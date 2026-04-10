from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse
import re


ROOT = Path(__file__).resolve().parents[1]
TARGET_CATEGORIES = {"tooling", "training", "applications"}


def parse_frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    meta = {}
    for line in text[4:end].splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            meta[k] = v
    return meta, text[end + 5 :]


def format_frontmatter(meta: dict):
    lines = ["---"]
    for key in ["title", "aliases", "category", "page_type", "project", "tags", "sources", "created", "updated"]:
        value = meta.get(key)
        if value is None:
            continue
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(value)}]")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def parse_sources(meta: dict):
    raw = meta.get("sources", "")
    if raw.startswith("[") and raw.endswith("]"):
        return [x.strip() for x in raw[1:-1].split(",") if x.strip()]
    return []


def extract_packet_summary(body: str):
    definition = ""
    why = ""
    capture = False
    for line in body.splitlines():
        if line.startswith("## 2026년 4월 큐레이션 요약"):
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture and line.startswith("- 정의:"):
            definition = line.split(":", 1)[1].strip()
        if capture and line.startswith("- 왜 중요한가:"):
            why = line.split(":", 1)[1].strip()
    return definition, why


def extract_source_domains(body: str):
    return re.findall(r"\(`([^`]+)`\): https?://", body)


def section_block(meta: dict, body: str):
    definition, why = extract_packet_summary(body)
    domains = extract_source_domains(body)
    domain_summary = ", ".join(sorted(dict.fromkeys(domains[:5]))) if domains else "공식 문서 / 논문 / 구현체"
    title = meta.get("title", "")
    page_type = meta.get("page_type", "")

    if page_type == "entity":
        return "\n".join(
            [
                "## 핵심 포인트",
                "",
                f"{title}는 단일 announcement보다 **공식 릴리스 글, 구현 문서, 벤치마크/평가 자료**를 함께 읽어야 성격이 드러나는 유형이다. 이번 수집본에서도 `{domain_summary}` 같은 서로 다른 source 층위가 함께 나타난다.",
                "",
                "1. **공식 발표**는 무엇이 새로 추가되었는지 말해 준다.",
                "2. **구현/SDK/문서**는 실제로 어디에 적용 가능한지 보여 준다.",
                "3. **벤치마크/비교 자료**는 marketing claim을 현실 사용 맥락으로 번역해 준다.",
                "",
                "## 실무 관점",
                "",
                f"{why} 따라서 이 항목을 실제 의사결정에 쓸 때는 '성능 수치 하나'보다 **지원 범위, 운영 제약, 비교 기준**을 같이 보는 편이 안전하다. 특히 제품/모델/프레임워크형 entity는 릴리스 직후보다 후속 release notes와 운영 사례가 더 중요해지는 경우가 많다.",
                "",
            ]
        )

    if page_type == "project-internal":
        return "\n".join(
            [
                "## 프로젝트 맥락",
                "",
                f"{title}는 일반 개념이라기보다 특정 제품 내부에서 의미가 생기는 기능 스냅샷이다. 그래서 이 문서는 '정의'보다 **프로젝트 안에서 어떤 문제를 해결하는가**를 중심으로 읽는 편이 맞다.",
                "",
                "## 운영 관점",
                "",
                f"{why} 이런 유형은 제품 버전 변화에 민감하므로, 이후 심화 작업에서는 changelog / docs / 구현 예시를 함께 추적해야 한다.",
                "",
            ]
        )

    if page_type == "summary":
        return "\n".join(
            [
                "## 읽는 순서",
                "",
                "이 요약 페이지는 source를 한 장으로 압축한 허브다. 먼저 큐레이션 요약으로 전체 흐름을 잡고, 그 다음 source 기반 참고에서 실제 원문을 따라가면 된다.",
                "",
                "## 실무 관점",
                "",
                f"{why} 따라서 이 문서는 결론을 확정하는 문서라기보다, **어떤 원문을 어떤 순서로 읽어야 하는지 안내하는 네비게이션 문서**로 쓰는 것이 적절하다.",
                "",
            ]
        )

    return "\n".join(
        [
            "## 핵심 메커니즘",
            "",
            f"{definition} 이 유형의 topic은 보통 하나의 제품보다 **반복 가능한 패턴 / 평가 기준 / 설계 trade-off**로 읽는 편이 유용하다. 이번 source 묶음에서도 `{domain_summary}`가 함께 나오면서 개념, 구현, 평가가 연결되어 있다.",
            "",
            "## 실무 관점",
            "",
            f"{why} 실무에서는 이 개념을 단독으로 쓰기보다 인접 개념과 묶어서 적용한다. 따라서 아래 source 기반 참고를 따라가며 어떤 source가 정의를 제공하고, 어떤 source가 구현/운영 힌트를 주는지 구분해 읽는 것이 좋다.",
            "",
        ]
    )


def deepen(path: Path):
    meta, body = parse_frontmatter(path)
    if meta.get("category") not in TARGET_CATEGORIES:
        return False
    if "raw/2026-04-10-hot-ai-topics-100.md" not in body and "raw/2026-04-10-hot-ai-topics-100.md" not in meta.get("sources", ""):
        return False
    if "## source 기반 참고" not in body:
        return False

    block = section_block(meta, body)
    body = re.sub(r"\n## (핵심 포인트|핵심 메커니즘|실무 관점|프로젝트 맥락|운영 관점|읽는 순서).*?(?=\n## |\Z)", "", body, flags=re.S)
    body = body.replace("## source 기반 참고", block + "\n## source 기반 참고", 1)
    path.write_text(format_frontmatter(meta) + "\n" + body.lstrip())
    return True


def main():
    changed = 0
    for path in sorted((ROOT / "wiki").rglob("*.md")):
        changed += int(deepen(path))
    print(f"changed={changed}")


if __name__ == "__main__":
    main()
