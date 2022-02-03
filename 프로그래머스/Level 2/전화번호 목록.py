# -*- coding: utf-8 -*-
"""

# 전화번호 목록
"""

phone_Book = ["119", "97674223", "1195524421"]
phone_Book =["12","123","1235","567","88"]

def solution(phone_Book):
    phone_Book = sorted(phone_Book)
    for p1, p2 in zip(phone_Book, phone_Book[1:]):
        print('p1 =', p1 , 'p2 = ', p2)
        if p2.startswith(p1):
            return False
    return True

solution(phoneBook)