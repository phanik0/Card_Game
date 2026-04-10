import streamlit as st
import time
import state
import game_logic

# 1. 페이지 설정
st.set_page_config(page_title="카드 맞추기 게임", page_icon="🃏", layout="centered")

st.title("🃏 카드 뒤집기 기억력 게임")

# 2. 상태 초기화
state.init_state()

# 3. 게임 종료 확인 및 상단 UI 배치
col1, col2 = st.columns([3, 1])
if st.session_state.game_over:
    col1.success("🎉 모든 카드를 맞췄습니다! 축하합니다!")
else:
    col1.info("카드를 클릭해서 같은 그림의 짝을 찾아보세요.")

# 다시 시작 버튼
if col2.button("다시 시작", use_container_width=True):
    state.reset_game()
    st.rerun()

st.markdown("---")

# 편의성을 위해 상태 변수 단축 할당
board = st.session_state.board
flipped = st.session_state.flipped
matched = st.session_state.matched

# 4. 4x4 카드 보드 그리기
cols = st.columns(4)

for i in range(16):
    col = cols[i % 4]
    
    if i in matched:
        # 이미 맞춘 카드 (앞면 표시, 클릭 비활성화)
        col.button(board[i], key=f"matched_{i}", disabled=True, use_container_width=True)
    elif i in flipped:
        # 현재 뒤집혀 있는 카드 (앞면 표시, 클릭 비활성화)
        col.button(board[i], key=f"flipped_{i}", disabled=True, use_container_width=True)
    else:
        # 뒷면인 카드를 클릭했을 때의 동작
        if col.button("❓", key=f"card_{i}", use_container_width=True):
            st.session_state.flipped.append(i)
            st.rerun()

# 5. 카드 매칭 확인 로직 (두 장이 뒤집힌 직후 검사)
if len(st.session_state.flipped) == 2:
    idx1 = st.session_state.flipped[0]
    idx2 = st.session_state.flipped[1]
    
    # 두 번째 카드가 렌더링 된 후, 사용자가 잠깐 볼 수 있도록 0.5초 대기
    time.sleep(0.5)
    
    card1 = board[idx1]
    card2 = board[idx2]
    
    # 규칙: 같으면 유지(matched에 추가), 다르면 다시 닫기
    if game_logic.check_match(card1, card2):
        st.session_state.matched.update([idx1, idx2])
        
        # 16장을 모두 맞췄다면 게임 종료 상태로 변경
        if len(st.session_state.matched) == 16:
            st.session_state.game_over = True
            
    # 다음 턴을 위해 뒤집힌 카드 목록 비우기 (UI 업데이트 예약)
    st.session_state.flipped = []
    st.rerun()
