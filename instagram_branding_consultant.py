import streamlit as st

st.title("Instagram 개인 브랜딩 컨설턴트 (누구나 쉽게 버전)")

st.write("초보자도 제대로 SNS 브랜딩할 수 있도록 설계됐어요. 각 질문에 솔직히 답하세요. 모르면 예시를 참고하거나 Enter 누르세요 – 추천 기본값이 적용돼요!")

# 질문 입력 폼 (20개: placeholder로 가이드 추가)
with st.form(key="branding_form"):
    name = st.text_input("1. 브랜드 이름은? (예: 그로스진 – 간단하고 기억에 남는 이름 추천)", placeholder="브랜드 이름 예: '그로스진' 또는 'MyDietCoach'")
    theme = st.text_input("2. 주요 주제는? (예: 다이어트 – 한 가지 니치에 집중하세요)", placeholder="주제 예: '다이어트', '피트니스', '여행' – 초보자 팁: 관심 있는 한 가지 선택")
    audience = st.text_input("3. 타겟 오디언스는? (예: 30-40대 여성 – 연령, 성별, 관심사)", placeholder="타겟 예: '30-40대 여성, 바쁜 직장인' – 연구 팁: 설문으로 파악")
    core_message = st.text_input("4. 핵심 메시지는? (예: 당신도 살 뺄 수 있다 – 공감 유발 메시지)", placeholder="메시지 예: '지속 가능한 다이어트' – 팁: 긍정적이고 영감 주는 것")
    followers = st.text_input("5. 현재 팔로워 수는? (숫자 또는 '초보' – 목표 설정에 도움)", placeholder="팔로워 예: '100' 또는 '초보' – 초보자라면 0부터 시작 OK")
    post_frequency = st.text_input("6. 주 게시 빈도는? (예: 3-5회 – 일관성 중요)", placeholder="빈도 예: '주 3회' – 팁: 초보자라면 주 2-3회부터")
    content_types = st.text_input("7. 컨텐츠 유형은? (예: 릴스, 스토리 – 시각적 콘텐츠 추천)", placeholder="유형 예: '릴스, 포스트, 스토리' – 팁: 릴스부터 시작")
    persona = st.text_input("8. 페르소나는? (예: 친근한 코치 – 당신의 개성)", placeholder="페르소나 예: '친근한 다이어트 코치' – 팁: 진짜 자신 반영")
    content_style = st.text_input("9. 콘텐츠 스타일은? (예: 교육적 – 정보 제공 위주)", placeholder="스타일 예: '교육적, 재미있는' – 팁: 스토리텔링 추가")
    color_theme = st.text_input("10. 색상 테마는? (예: 파스텔 – 일관성 유지)", placeholder="색상 예: '파란색, 밝은 톤' – 팁: 브랜드 느낌 맞춤")
    design_style = st.text_input("11. 디자인 스타일은? (예: 미니멀 – 깔끔하게)", placeholder="디자인 예: '미니멀, 현대적' – 팁: Canva로 쉽게")
    goals = st.text_input("12. 주요 목표는? (예: 팔로워 증가 – SMART 목표 설정)", placeholder="목표 예: '3개월 내 1000명 팔로워' – 팁: 측정 가능하게")
    challenges = st.text_input("13. 도전 과제는? (예: 아이디어 고갈 – 극복 팁 공유)", placeholder="도전 예: '콘텐츠 아이디어 부족' – 팁: 브레인스토밍")
    collaborations = st.text_input("14. 콜라보 계획은? (예: 다른 인플루언서 – 네트워킹)", placeholder="콜라보 예: '피트니스 계정과' – 팁: 초기에는 DM으로 시작")
    uvp = st.text_input("15. 고유 가치 제안(UVP)은? (예: 독창적 팁 – 차별화 포인트)", placeholder="UVP 예: '30대 여성 맞춤 10분 루틴' – 팁: 독특한 가치 강조")
    audience_research = st.text_input("16. 타겟 오디언스 연구 결과? (예: 설문 통해 관심사 파악 – 경쟁자 분석)", placeholder="연구 예: '바쁜 엄마 식단 관심' – 팁: Insights 사용")
    content_calendar = st.text_input("17. 콘텐츠 캘린더 계획? (예: 월별 테마 – 일관성)", placeholder="캘린더 예: '1월: 기본 식단' – 팁: Google Calendar로 관리")
    engagement_strategy = st.text_input("18. 참여 전략은? (예: Q&A 세션 – 댓글 응답)", placeholder="참여 예: '스토리 폴, DM 응답' – 팁: 매일 30분 할애")
    analytics_tools = st.text_input("19. 분석 도구 계획? (예: Instagram Insights – 성과 측정)", placeholder="도구 예: 'Insights, Google Analytics' – 팁: 주간 리뷰")
    branding_confusion = st.text_input("20. 브랜딩에서 가장 혼란스러운 점? (예: 테마 선택 – 브레인스토밍 팁)", placeholder="혼란 예: '콘텐츠 어떻게 만들지' – 팁: 10일 챌린지")
    submit_button = st.form_submit_button(label="전문 전략 생성")

if submit_button:
    # 입력 유효성 체크 (빈 입력 경고)
    if not name or not theme:
        st.warning("브랜드 이름과 주제는 필수예요! 기본값으로 진행하지만, 다시 입력 추천.")
    
    # 기본값 설정 (더 구체적으로 업그레이드)
    if not name: name = "개인 브랜드 (예: MyBrand)"
    if not theme: theme = "라이프스타일 (니치 추천: 한 가지에 집중)"
    if not audience: audience = "20-30대 젊은 층 (연구 추천: 설문으로 관심사 파악)"
    if not core_message: core_message = "긍정적 영감 (공감 유발 메시지 추천)"
    followers = 0 if (followers.lower() == '초보' or not followers.isdigit()) else int(followers)
    if not post_frequency: post_frequency = "주 3-5회 (일관성 유지 팁)"
    if not content_types: content_types = "릴스와 포스트 (시각 콘텐츠 위주)"
    if not persona: persona = "친근한 전문가 (진짜 자신 반영)"
    if not content_style: content_style = "교육적이고 재미있는 (스토리텔링 추가)"
    if not color_theme: color_theme = "밝은 톤 (일관성 유지)"
    if not design_style: design_style = "미니멀하고 깔끔한 (Canva 추천)"
    if not goals: goals = "팔로워 증가와 engagement 높이기 (SMART 목표 설정)"
    if not challenges: challenges = "시간 관리 (브레인스토밍으로 극복)"
    if not collaborations: collaborations = "초기에는 비슷한 계정 DM (네트워킹 시작)"
    if not uvp: uvp = "독창적 콘텐츠 제공 (차별화 포인트)"
    if not audience_research: audience_research = "설문이나 경쟁자 분석 추천 (Insights 활용)"
    if not content_calendar: content_calendar = "월별 테마 계획 세우기 (e.g., 1월: 기본 팁)"
    if not engagement_strategy: engagement_strategy = "댓글 응답과 폴 (매일 30분 참여)"
    if not analytics_tools: analytics_tools = "Instagram Insights (주간 메트릭스 리뷰)"
    if not branding_confusion: branding_confusion = "테마 정의부터 시작 (10일 챌린지 추천)"

    # 추천 계정 기능 (테마 기반 확장, 서치 결과 반영)
    recommended_accounts = """
[참고할 Instagram 계정 추천 (브랜딩 인스피레이션)]
- 일반 추천: @thechrisdo (브랜딩 코치, 비즈니스 팁), @jennakutcher (진정성 스토리텔링), @garyvee (모티베이션, 콘텐츠 전략).
"""
    if "다이어트" in theme.lower() or "diet" in theme.lower() or "fitness" in theme.lower():
        recommended_accounts += "- 테마 맞춤: @kayla_itsines (여성 피트니스 챌린지), @toneitup (30-40대 워크아웃), @nutritionstripped (건강 식단)."
    elif "여행" in theme.lower() or "travel" in theme.lower():
        recommended_accounts += "- 테마 맞춤: @beautifuldestinations (여행지 공유), @natgeotravel (모험 스토리)."
    else:
        recommended_accounts += "- 당신의 테마('" + theme + "')에 맞게 검색: 'best Instagram accounts for " + theme + " branding'."
    recommended_accounts += "\n이 계정들을 팔로우하며 콘텐츠 아이디어, 참여 방식 배우세요. (웹 서치 기반 추천)"

    # 브랜딩 전략 (업그레이드: 더 구체적, 서치 반영)
    branding = f"""
[전문 브랜딩 컨설팅]
- 브랜드 이름: {name} (팁: 바이오에 포함, 기억에 남게)
- 주요 주제: {theme} (니치 팁: 한 가지에 집중, 초보자라면 관심사부터)
- 타겟 오디언스: {audience} (연구 팁: {audience_research} – Insights나 설문으로 관심사 파악, 경쟁자 분석 추천)
- 핵심 메시지: {core_message} (강화 팁: 공감 유발, e.g., '바쁜 일상 속 변화')
- UVP (고유 가치 제안): {uvp} (차별화 팁: 독특한 팁 공유, e.g., '30대 맞춤 루틴')
- 페르소나/스타일: {persona}, {content_style}, {color_theme}/{design_style} (팁: 일관성 유지, 스토리텔링으로 인간미 더하기)
- 목표/도전: {goals}, {challenges} 극복 (혼란스러운 점: {branding_confusion} – 해결: 주간 브레인스토밍, 10일 챌린지 시작)
- 전문 팁: 일관성 유지 (매일 테마 맞춰 포스트), 스토리텔링 (개인 여정 공유), 바이오에 UVP 포함. 네트워킹: {collaborations}. KPI: reach, engagement 추적.
"""

    # 단기 전략 (더 구체적: 예시 확장)
    short_term = f"""
[단기 전략: 1-3개월 - 기반 다지기 (초보자 포커스)]
- 목표: {goals} 초점, 기본 팔로워 {followers * 2 if followers > 0 else 500}명 달성 (SMART 설정).
- 콘텐츠 기획: 주 {post_frequency} {content_types} ({content_calendar}로 계획 – e.g., 주 1: 소개).
- 예시 아이디어:
  1. 소개 시리즈: '{name}의 {uvp}' 릴스 (before/after 스토리).
  2. {audience} 공감 콘텐츠: '{core_message} 실천 팁' + {engagement_strategy} (e.g., 폴: '오늘 식단?').
  3. 스토리: 매일 Q&A나 뒤집기 (참여 유도).
- 전문 팁: Insights로 참여율 분석, A/B 테스트 (해시태그 비교). 초기 챌린지: 10일 매일 포스트 (테마 브레인스토밍).
"""

    # 중기 전략
    mid_term = f"""
[중기 전략: 3-6개월 - 성장 가속]
- 목표: engagement 높이기, {collaborations} 시작 (e.g., 게스트 포스트).
- 콘텐츠 기획: {content_calendar} 확장, 시리즈 콘텐츠 ({content_style} 강조).
- 예시 아이디어:
  1. 챌린지 시리즈: '{theme} 30일 챌린지' (일일 팁 + 참여 유도).
  2. 콜라보: {audience} 비슷한 계정과 공동 릴스.
  3. 분석 기반: {analytics_tools}로 인기 콘텐츠 반복 (e.g., 조회수 높은 스타일).
- 전문 팁: 트렌드 릴스 (인기 음악 사용), 소액 광고 (타겟: {audience}), 커뮤니티 빌딩 (DM 응답률 높이기).
"""

    # 장기 전략
    long_term = f"""
[장기 전략: 6개월 이상 - 지속 가능성 확보]
- 목표: {goals} 달성, 수익화 준비 (e.g., 제휴 마케팅).
- 콘텐츠 기획: {content_calendar} + 라이브/IGTV ({engagement_strategy} 확대).
- 예시 아이디어:
  1. 깊이 있는 콘텐츠: '{uvp} 가이드' e-book 공유 (무료 다운로드로 이메일 수집).
  2. 커뮤니티 빌딩: {audience} 이벤트 (온라인 미팅이나 챌린지).
  3. 장기 시리즈: '{core_message} 1년 여정'回顾 (성공 스토리 공유).
- 전문 팁: 월간 리뷰 ({analytics_tools}, KPI: conversion rate), {challenges} 모니터링. 모네타이제이션: 제휴/코칭 시작.
"""

    # 전체 출력
    st.write("### 생성된 전문 컨설팅 전략")
    st.write(branding)
    st.write(short_term)
    st.write(mid_term)
    st.write(long_term)
    st.write(recommended_accounts)
    st.write("이 전략은 웹/X 기반 전문 가이드에서 추출한 팁을 반영했어요. 실제 적용하며 조정하세요! (일관성 + 참여가 핵심)")

    # 추가 기능: 결과 다운로드
    result_text = branding + short_term + mid_term + long_term + recommended_accounts
    st.download_button("전략 다운로드 (TXT)", result_text, file_name="my_branding_strategy.txt")
    if st.button("다시 시작"):
        st.experimental_rerun()
