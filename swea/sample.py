if arr[r][c] == 1:
    if i == 0:
        continue
    elif i == 1:
        continue
    elif i == 2:
        continue
    else:
        continue
if i % 2 == 0:
    if arr[nr][nc] == 2 and (arr[nr][nc] == 4 or arr[nr][nc] == 7):
        continue
    elif arr[r][c] == 3 and (arr[nr][nc] == 6 or arr[nr][nc] == 7):
        continue
    elif arr[r][c] == 4 and (arr[nr][nc] == 3 or arr[nr][nc] == 7):
        continue
    elif arr[r][c] == 5 and (arr[nr][nc] == 3 or arr[nr][nc] == 6):
        continue
    elif arr[r][c] == 6 and (arr[nr][nc] == 5 or arr[nr][nc] == 3):
        continue
    elif arr[r][c] == 7 and (arr[nr][nc] == 4 or arr[nr][nc] == 3):
        continue
else:
    if arr[r][c] == 2 and (arr[nr][nc] == 5 or arr[nr][nc] == 6):
        continue
    elif arr[r][c] == 3 and (arr[nr][nc] == 4 or arr[nr][nc] == 5):
        continue
    elif arr[r][c] == 4 and (arr[nr][nc] == 2 or arr[nr][nc] == 5):
        continue
    elif arr[r][c] == 5 and (arr[nr][nc] == 4 or arr[nr][nc] == 2):
        continue
    elif arr[r][c] == 6 and (arr[nr][nc] == 2 or arr[nr][nc] == 7):
        continue
    elif arr[r][c] == 7 and (arr[nr][nc] == 6 or arr[nr][nc] == 2):
        continue
if arr[r][c] == 2 and arr[nr][nc] == 3:
    continue
if arr[r][c] == 3 and arr[nr][nc] == 2:
    continue