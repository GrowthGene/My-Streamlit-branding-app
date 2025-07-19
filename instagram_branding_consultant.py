import streamlit as st

st.title("Instagram 개인 브랜딩 컨설턴트 (전문 업그레이드 버전)")

st.write("브랜딩 방향을 잡기 어려운 초보자를 위해 설계된 도구예요. 20개 질문을 통해 맞춤 전략을 생성합니다. 모르면 Enter 누르세요.")

# 질문 입력 폼 (총 20개: 더 디테일하게 확장)
with st.form(key="branding_form"):
    name = st.text_input("1. 브랜드 이름은? (예: YourName)")
    theme = st.text_input("2. 주요 주제는? (예: 피트니스, 여행)")
    audience = st.text_input("3. 타겟 오디언스는? (예: 20대 여성)")
    core_message = st.text_input("4. 핵심 메시지는? (예: 건강한 삶)")
    followers = st.text_input("5. 현재 팔로워 수는? (숫자 또는 '초보')")
    post_frequency = st.text_input("6. 주 게시 빈도는? (예: 3-5회)")
    content_types = st.text_input("7. 컨텐츠 유형은? (예: 릴스, 스토리)")
    persona = st.text_input("8. 페르소나는? (예: 친근한 전문가)")
    content_style = st.text_input("9. 컨텐츠 스타일은? (예: 교육적)")
    color_theme = st.text_input("10. 색상 테마는? (예: 파스텔)")
    design_style = st.text_input("11. 디자인 스타일은? (예: 미니멀)")
    goals = st.text_input("12. 주요 목표는? (예: 팔로워 증가)")
    challenges = st.text_input("13. 도전 과제는? (예: 아이디어 고갈)")
    collaborations = st.text_input("14. 콜라보 계획은? (예: 다른 인플루언서)")
    uvp = st.text_input("15. 고유 가치 제안(UVP)은? (예: 독창적 팁 제공)")  # 새로 추가: UVP
    audience_research = st.text_input("16. 타겟 오디언스 연구 결과? (예: 설문 통해 알게 된 관심사)")  # 새로 추가
    content_calendar = st.text_input("17. 콘텐츠 캘린더 계획? (예: 월별 테마)")  # 새로 추가
    engagement_strategy = st.text_input("18. 참여 전략은? (예: Q&A 세션)")  # 새로 추가
    analytics_tools = st.text_input("19. 분석 도구 계획? (예: Instagram Insights)")  # 새로 추가
    branding_confusion = st.text_input("20. 브랜딩에서 가장 혼란스러운 점? (예: 테마 선택 어려움)")  # 새로 추가: 갈피 못 잡는 부분 대처
    submit_button = st.form_submit_button(label="전문 전략 생성")

if submit_button:
    # 기본값 설정 (초보자 친화적)
    if not name: name = "개인 브랜드"
    if not theme: theme = "라이프스타일"
    if not audience: audience = "20-30대 젊은 층"
    if not core_message: core_message = "긍정적 영감"
    followers = 0 if (followers.lower() == '초보' or not followers.isdigit()) else int(followers)
    if not post_frequency: post_frequency = "3-5회"
    if not content_types: content_types = "릴스와 포스트"
    if not persona: persona = "친근한"
    if not content_style: content_style = "교육적"
    if not color_theme: color_theme = "밝은 톤"
    if not design_style: design_style = "미니멀"
    if not goals: goals = "팔로워 증가"
    if not challenges: challenges = "시간 관리"
    if not collaborations: collaborations = "초기 없음"
    if not uvp: uvp = "독창적 콘텐츠 제공"
    if not audience_research: audience_research = "기본 설문 추천"
    if not content_calendar: content_calendar = "월별 계획 세우기"
    if not engagement_strategy: engagement_strategy = "댓글 응답과 폴"
    if not analytics_tools: analytics_tools = "Instagram Insights"
    if not branding_confusion: branding_confusion = "테마 정의부터 시작"

    # 추천 계정 기능 (웹 서치 기반 하드코딩 + 동적)
    recommended_accounts = """
[참고할 Instagram 계정 추천 (브랜딩 인스피레이션)]
- @thechrisdo: 개인 브랜딩 코치, 비즈니스 팁 공유.
- @jennakutcher: 포토그래퍼/팟캐스터, 진정성 있는 스토리텔링.
- @jasminestar: 비즈니스 코치, 전략적 콘텐츠.
- @stefaniabrunoriofficial: 콘텐츠 마케팅 전문가, 목적 지향 브랜딩.
- @noraborealis: 작가, 감성적 개인 이야기.
- @lejuanjames: 코미디언, 문화적 브랜딩.
- 당신의 테마에 맞게 검색: 'best Instagram for [theme] branding'.
이 계정들을 팔로우하며 UVP, 콘텐츠 스타일, 참여 방식을 배우세요.
"""

    # 브랜딩 전략 (더 디테일: UVP, 연구 등 추가)
    branding = f"""
[전문 브랜딩 컨설팅]
- 브랜드 이름: {name}
- 주요 주제: {theme}
- 타겟 오디언스: {audience} (연구 팁: {audience_research} – 설문이나 경쟁자 분석으로 시작하세요)
- 핵심 메시지: {core_message}
- UVP (고유 가치 제안): {uvp} (이걸 중심으로 차별화하세요)
- 페르소나/스타일: {persona}, {content_style}, {color_theme}/{design_style}
- 목표/도전: {goals}, {challenges} 극복 (혼란스러운 점: {branding_confusion} – 브레인스토밍으로 해결)
- 전문 팁: 일관성 유지 (매일 테마 맞춰 포스트), 스토리텔링 활용, 바이오에 UVP 포함. 갈피 못 잡을 때: 10일 챌린지로 시작 (예: 매일 테마 관련 포스트).
"""

    # 단기 전략 (더 구체적: 콘텐츠 캘린더 등)
    short_term = f"""
[단기 전략: 1-3개월 - 기반 다지기 (초보자 포커스)]
- 목표: {goals} 초점, 기본 팔로워 2배 증가.
- 콘텐츠 기획: 주 {post_frequency} {content_types} ({content_calendar}로 계획 세우기).
- 예시 아이디어:
  1. 소개 시리즈: '{name}의 {uvp}' 릴스.
  2. {audience} 공감 콘텐츠: {core_message} 팁 + {engagement_strategy}.
  3. 스토리: 매일 폴/Q&A.
- 전문 팁: Insights로 참여율 분석, A/B 테스트 (예: 다른 해시태그 비교). 초기 10일 챌린지: 테마 브레인스토밍.
"""

    # 중기 전략
    mid_term = f"""
[중기 전략: 3-6개월 - 성장 가속]
- 목표: engagement 높이기, {collaborations} 시작.
- 콘텐츠 기획: {content_calendar} 확장, 시리즈 콘텐츠.
- 예시 아이디어:
  1. 챌린지: '{theme} 30일 챌린지' ({content_style}).
  2. 콜라보: {audience} 비슷한 계정과.
  3. 분석: {analytics_tools}로 인기 콘텐츠 반복.
- 전문 팁: 트렌드 릴스 활용, 광고 소액 투자, 커뮤니티 빌딩 (DM 응답률 높이기).
"""

    # 장기 전략
    long_term = f"""
[장기 전략: 6개월 이상 - 지속/수익화]
- 목표: {goals} 달성, 브랜드 파트너십.
- 콘텐츠 기획: {content_calendar} + 라이브/IGTV.
- 예시 아이디어:
  1. 전문 시리즈: '{uvp} 가이드' e-book 공유.
  2. 이벤트: {audience} 오프라인/온라인 미팅.
  3.回顾: 1년 {core_message} 여정.
- 전문 팁: 월간 메트릭스 리뷰 ({analytics_tools}), {challenges} 모니터링, 모네타이제이션 (제휴 마케팅 시작).
"""

    # 출력
    st.write("### 생성된 전문 컨설팅 전략")
    st.write(branding)
    st.write(short_term)
    st.write(mid_term)
    st.write(long_term)
    st.write(recommended_accounts)
    st.write("이 전략은 웹 기반 전문 가이드에서 추출한 팁을 반영했어요. 실제 적용하며 조정하세요!")
