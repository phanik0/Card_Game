import random

def create_board():
    """
    8쌍의 이모지 카드를 생성하고 섞어서 16장의 보드 리스트를 반환합니다.
    """
    emojis = ['🍎', '🍌', '🍇', '🍉', '🍓', '🍒', '🍍', '🥝']
    deck = emojis * 2  # 8쌍, 총 16장
    random.shuffle(deck)
    return deck

def check_match(card1, card2):
    """
    두 카드의 값이 같은지 비교합니다.
    """
    return card1 == card2
