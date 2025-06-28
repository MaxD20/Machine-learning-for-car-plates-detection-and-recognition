import cv2

def draw_label(frame, text, x1, y1,
               padding=10, font_scale=1.2,
               font=cv2.FONT_HERSHEY_SIMPLEX,
               thickness=3):

    text_box_h = 50
    (tw, th), base = cv2.getTextSize(text, font, font_scale, thickness)
    text_box_w = tw + 2 * padding

    x1, y1 = int(x1), int(y1)
    x2, y2 = x1 + text_box_w, y1 - text_box_h

    # background
    cv2.rectangle(frame, (x1, y2), (x2, y1), (0, 255, 0), -1)

    # text (shadow then foreground)
    shadow = 2
    tx = x1 + padding
    ty = y2 + (text_box_h + th) // 2 + base // 2
    cv2.putText(frame, text, (tx + shadow, ty + shadow), font, font_scale, (0, 0, 0), 5)
    cv2.putText(frame, text, (tx, ty), font, font_scale, (255, 255, 255), thickness)
