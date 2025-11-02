#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

int main() {
    int dwarf[9];
    int sum = 0;

    for (int i = 0; i < 9; i++) {
        scanf("%d", &dwarf[i]);
        sum += dwarf[i];
    }

    int fake1, fake2;
    for (int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (sum - dwarf[i] - dwarf[j] == 100) {
                fake1 = i;
                fake2 = j;
                goto end; // 정답 찾으면 반복문 탈출
            }
        }
    }

end:
    int result[7], idx = 0;
    for (int i = 0; i < 9; i++) {
        if (i == fake1 || i == fake2) continue;
        result[idx++] = dwarf[i];
    }

    qsort(result, 7, sizeof(int), compare);
    for (int i = 0; i < 7; i++) printf("%d\n", result[i]);
    return 0;
}
