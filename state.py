import streamlit as st
import game_logic

def init_state():
    """게임 상태를 초기화합니다."""
    if "board" not in st.session_state:
        st.session_state.board = game_logic.create_board()
    
    if "flipped" not in st.session_state:
        # 현재 뒤집힌 카드의 인덱스를 저장 (최대 2장)
        st.session_state.flipped = []
        
    if "matched" not in st.session_state:
        # 이미 짝을 맞춘 카드의 인덱스를 저장
        st.session_state.matched = set()
        
    if "game_over" not in st.session_state:
        # 게임 종료 여부
        st.session_state.game_over = False

def reset_game():
    """게임을 다시 시작할 수 있도록 상태를 초기화(리셋)합니다."""
    st.session_state.board = game_logic.create_board()
    st.session_state.flipped = []
    st.session_state.matched = set()
    st.session_state.game_over = False
