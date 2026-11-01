#!/usr/bin/env python3
"""统计讲解稿各节字数与预估时长。

用法:
    python3 scripts/script_stats.py 讲解稿.md
    python3 scripts/script_stats.py 讲解稿.md --wpm 190
"""
import argparse
import re

CJK = re.compile(r"[\u4e00-\u9fff]")
MARK = re.compile(r"【[^】]*】")
ACTION = re.compile(r"（[^）]*）|\([^)]*\)")
HEADER = re.compile(r"\[[^\]]*\]")


def clean(text: str) -> str:
    """去掉待补标记、动作提示、节头时长标注，只留可念的字。"""
    text = MARK.sub("", text)
    text = ACTION.sub("", text)
    text = HEADER.sub("", text)
    return text


def cjk_len(text: str) -> int:
    return len(CJK.findall(text))


def main() -> None:
    ap = argparse.ArgumentParser(description="讲解稿字数与时长统计")
    ap.add_argument("path", help="讲解稿 markdown 文件")
    ap.add_argument("--wpm", type=int, default=200, help="语速，字/分钟，默认 200")
    args = ap.parse_args()

    sections = []
    title, buf = "（篇首）", []
    with open(args.path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("## "):
                if buf:
                    sections.append((title, "".join(buf)))
                title, buf = line[3:].strip(), []
            else:
                buf.append(line)
    if buf:
        sections.append((title, "".join(buf)))

    total = 0
    print(f"{'节':<40}{'字数':>7}{'时长':>12}")
    print("-" * 60)
    for name, body in sections:
        n = cjk_len(clean(body))
        total += n
        minutes, seconds = divmod(round(n / args.wpm * 60), 60)
        print(f"{name[:38]:<40}{n:>7}{minutes:>7}分{seconds:02d}秒")
    print("-" * 60)
    minutes, seconds = divmod(round(total / args.wpm * 60), 60)
    print(f"{'合计':<40}{total:>7}{minutes:>7}分{seconds:02d}秒")


if __name__ == "__main__":
    main()
