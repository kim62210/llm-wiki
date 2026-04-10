from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
TARGET_CATEGORIES = {"agents", "concepts", "inference", "rag"}


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


def packet_summary(body: str):
    definition = ""
    why = ""
    domains = []
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
        if capture and line.startswith("- 주요 도메인:"):
            domains = [x.strip() for x in line.split(":", 1)[1].split(",") if x.strip()]
    return definition, why, domains


def block(meta: dict, body: str):
    definition, why, domains = packet_summary(body)
    domain_text = ", ".join(domains[:5]) if domains else "논문 / 구현체 / 문서"
    title = meta.get("title", "")
    page_type = meta.get("page_type", "")
    category = meta.get("category", "")

    if category == "rag":
        return "\n".join(
            [
                "## 핵심 메커니즘",
                "",
                f"{definition} RAG 계열 토픽은 보통 하나의 검색 기법보다 **인덱싱 방식, 검색 인터페이스, 후처리·압축 전략**의 조합으로 이해해야 한다. 이번 source 묶음에서도 `{domain_text}`처럼 서로 다른 층위의 구현/연구 source가 함께 나타난다.",
                "",
                "## 운영 관점",
                "",
                f"{why} 실제 운영에서는 retrieval quality 하나만 보는 것이 아니라 latency, index 비용, update 빈도, multi-hop 질의 대응 여부를 함께 봐야 한다.",
                "",
            ]
        )

    if category == "inference":
        return "\n".join(
            [
                "## 핵심 메커니즘",
                "",
                f"{definition} 추론/서빙 토픽은 대부분 **throughput, latency, memory, hardware topology**의 trade-off에서 의미가 생긴다. source를 함께 보면 `{domain_text}`처럼 논문과 구현체/벤더 문서가 동시에 등장한다.",
                "",
                "## 구현·운영 관점",
                "",
                f"{why} 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.",
                "",
            ]
        )

    if category == "agents":
        return "\n".join(
            [
                "## 핵심 구조",
                "",
                f"{definition} 에이전트 토픽은 보통 모델 자체보다 **루프 구조, 상태 관리, 작업 분해, 검증 방식**이 핵심이다. 이번 source 묶음도 `{domain_text}`를 오가며 설계 패턴과 구현 사례를 함께 보여 준다.",
                "",
                "## 실무 관점",
                "",
                f"{why} 실무에서는 이 개념을 단독으로 적용하기보다 memory / planning / evaluation / harness 설계와 묶어서 도입하는 경우가 많다.",
                "",
            ]
        )

    if page_type == "entity":
        return "\n".join(
            [
                "## 핵심 포인트",
                "",
                f"{title}는 개념 설명보다 **어떤 역할을 하는 대상인지, 어떤 ecosystem 안에서 쓰이는지**가 중요하다. 수집 source도 `{domain_text}`처럼 제품/문서/비교 자료를 함께 포함한다.",
                "",
                "## 실무 관점",
                "",
                f"{why} 따라서 이 항목은 '정의'보다도 **도입 시점, 주변 도구와의 연결, 운영 제약**을 함께 보는 허브로 읽는 편이 맞다.",
                "",
            ]
        )

    return "\n".join(
        [
            "## 핵심 메커니즘",
            "",
            f"{definition} 이 개념은 단일 문장 정의보다 **어떤 failure mode를 설명하는지, 어떤 구조적 trade-off를 드러내는지**를 함께 볼 때 가치가 커진다.",
            "",
            "## 실무 관점",
            "",
            f"{why} 따라서 아래 source 기반 참고는 단순 참고 목록이 아니라, 정의·구현·평가가 어떤 순서로 연결되는지 읽는 용도로 활용하는 것이 좋다.",
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
    new_block = block(meta, body)
    body = re.sub(r"\n## (핵심 구조|핵심 포인트|핵심 메커니즘|실무 관점|운영 관점|구현·운영 관점).*?(?=\n## |\Z)", "", body, flags=re.S)
    body = body.replace("## source 기반 참고", new_block + "\n## source 기반 참고", 1)
    path.write_text(format_frontmatter(meta) + "\n" + body.lstrip())
    return True


def main():
    changed = 0
    for path in sorted((ROOT / "wiki").rglob("*.md")):
        changed += int(deepen(path))
    print(f"changed={changed}")


if __name__ == "__main__":
    main()
