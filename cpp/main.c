#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char ReadName(char name[30][100], long num[30], int score[30][6], int m,
              int n) {
    int i, j;
    for (i = 0; i < m; i++) {
        printf("Please input the name:");
        scanf("%s", name[i]);
        printf("Please input the number:");
        scanf("%ld", &num[i]);
        for (j = 1; j <= n; j++) {
            printf("Please input the score %d:", j);
            scanf("%d", &score[i][j - 1]);
        }
        getchar();
    }
}

int FindCourAve(int score[30][6], int m, int n) {
    int i, j, sum;
    float ave;
    for (i = 0; i < n; i++)  // i for different courses
    {
        for (j = 0, sum = 0; j < m; j++)  // j for different students
        {
            sum = sum + score[j][i];
        }
        ave = (float)sum / m;
        printf("The total score of course %d is %d.\n ", i + 1, sum);
        printf("The average score of the course %d is %.2f.\n", i + 1, ave);
    }
}

int FindStuAve(int score[30][6], long num[30], int m, int n, int sumstu[30]) {
    int i, j;
    float ave;
    for (i = 0; i < m; i++) {
        for (j = 0, sumstu[i] = 0; j < n; j++) {
            sumstu[i] = sumstu[i] + score[i][j];
        }
        ave = (float)sumstu[i] / n;
        printf("The total score of student %ld is %d.\n", num[i], sumstu[i]);
        printf("The average score of student %ld is %.2f.\n", num[i], ave);
    }
    return sumstu[30];
}

int Output(char name[30][100], long num[30], int score[30][6], int m, int n) {
    int i, j;
    for (i = 0; i < m; i++) {
        printf("\n%s  %ld  ", name[i], num[i]);
        for (j = 0; j < n; j++) {
            printf("%d  ", score[i][j]);
        }
    }
}

SortDesScore(int sumstu[30], long num[30], char name[30][100], int m,
             int rank[30]) {
    int i, j, temp;
    char str[100];
    for (i = 0; i < m - 1; i++) {
        for (j = i + 1; j < m; j++) {
            if (sumstu[i] <= sumstu[j]) {
                temp = sumstu[i];
                sumstu[i] = sumstu[j];
                sumstu[j] = temp;
                temp = num[i];
                num[i] = num[j];
                num[j] = temp;
                strcpy(str, name[i]);
                strcpy(name[i], name[j]);
                strcpy(name[j], str);
            }
        }
    }
    for (i = 0; i < m; i++) {
        rank[i] = i + 1;
    }
    for (i = 0; i < m; i++) {
        printf("%s  %ld  %d\n", name[i], num[i], sumstu[i]);
    }
    return rank[30];
}

int SortAscScore(int sumstu[30], long num[30], char name[30][100], int m) {
    int i, j, temp;
    char str[100];
    for (i = 0; i < m - 1; i++) {
        for (j = i + 1; j < m; j++) {
            if (sumstu[i] >= sumstu[j]) {
                temp = sumstu[i];
                sumstu[i] = sumstu[j];
                sumstu[j] = temp;
                temp = num[i];
                num[i] = num[j];
                num[j] = temp;
                strcpy(str, name[i]);
                strcpy(name[i], name[j]);
                strcpy(name[j], str);
            }
        }
    }
    for (i = 0; i < m; i++) {
        printf("%s  %ld  %d\n", name[i], num[i], sumstu[i]);
    }
}

int SortAscNum(long num[30], char name[30][100], int score[30][6], int m,
               int n) {
    int i, j, temp, k;
    char str[100];
    for (i = 0; i < m - 1; i++) {
        for (j = i + 1; j < m; j++) {
            if (num[i] >= num[j]) {
                temp = num[i];
                num[i] = num[j];
                num[j] = temp;
                for (k = 0; k < n; k++) {
                    temp = score[i][k];
                    score[i][k] = score[j][k];
                    score[j][k] = temp;
                }
                strcpy(str, name[i]);
                strcpy(name[i], name[j]);
                strcpy(name[j], str);
            }
        }
    }
    for (i = 0; i < m; i++) {
        printf("\n%s  %ld  ", name[i], num[i]);
        for (j = 0; j < n; j++) {
            printf("%d  ", score[i][j]);
        }
    }
}

int SortDicName(char name[30][100], long num[30], int score[30][6], int n,
                int m) {
    int i, j, temp, k;
    char str[100];
    for (i = 0; i < m; i++) {
        for (j = i + 1; j < m; j++) {
            if (strcmp(name[i], name[j]) > 0) {
                temp = num[i];
                num[i] = num[j];
                num[j] = temp;
                for (k = 0; k < n; k++) {
                    temp = score[i][k];
                    score[i][k] = score[j][k];
                    score[j][k] = temp;
                }
                strcpy(str, name[i]);
                strcpy(name[i], name[j]);
                strcpy(name[j], str);
            }
        }
    }
    for (i = 0; i < m; i++) {
        printf("\n%s  %ld  ", name[i], num[i]);
        for (j = 0; j < n; j++) {
            printf("%d  ", score[i][j]);
        }
    }
}

int SearbyName(char name[30][100], long num[30], int score[30][6], int m, int n,
               int rank[30]) {
    int i, j, find = 0;
    char thename[100];
    printf("Please input the name of the student you want to know the score:");
    scanf("%s", thename);
    for (i = 0; i < m; i++) {
        if (strcmp(name[i], thename) == 0) {
            find = 1;
            break;
        }
    }
    if (find == 1) {
        printf("\n%s  %ld  %d  ", name[i], num[i], rank[i]);
        for (j = 0; j < n; j++) {
            printf("%d  ", score[i][j]);
        }
    } else
        printf("Not find!");
}

int Searbynum(char name[30][100], long num[30], int score[30][6], int m, int n,
              int rank[30]) {
    int i, j, find = 0;
    long thenum;
    printf(
        "Please input the number of the student you want to know the score:");
    scanf("%ld", &thenum);
    for (i = 0; i < m; i++) {
        if (num[i] == thenum) {
            find = 1;
            break;
        }
    }
    if (find == 1) {
        printf("%s  %ld  %d  ", name[i], num[i], rank[i]);
        for (j = 0; j < n; j++) {
            printf("%d  ", score[i][j]);
        }
    } else
        printf("Not find!");
}

int Classify(int score[30][6], int m, int n) {
    float rateyx, ratelh, ratezd, ratejg, ratebjg;
    char c = '%';
    int i, j;
    for (j = 0; j < n; j++) {
        int yx = 0;
        int lh = 0;
        int zd = 0;
        int jg = 0;
        int bjg = 0;
        for (i = 0; i < m; i++) {
            if (score[i][j] >= 90 && score[i][j] <= 100)
                yx = yx + 1;
            else if (score[i][j] >= 80 && score[i][j] < 90)
                lh = lh + 1;
            else if (score[i][j] >= 70 && score[i][j] < 80)
                zd = zd + 1;
            else if (score[i][j] >= 60 && score[i][j] < 70)
                jg = jg + 1;
            else
                bjg = bjg + 1;
        }
        rateyx = (float)yx / m * 100;
        ratelh = (float)lh / m * 100;
        ratezd = (float)zd / m * 100;
        ratejg = (float)jg / m * 100;
        ratebjg = (float)bjg / m * 100;
        printf("For course %d:\n", j + 1);
        printf(
            "The sum of outstanding is %d,the rate of outstanding is %.2f%c.\n",
            yx, rateyx, c);
        printf("The sum of outstanding is %d,the rate of good is %.2f%c.\n", lh,
               ratelh, c);
        printf("The sum of outstanding is %d,the rate of medium is %.2f%c.\n",
               zd, ratezd, c);
        printf(
            "The sum of outstanding is %d,the rate of acceptable is %.2f%c.\n",
            jg, ratejg, c);
        printf("The sum of outstanding is %d,the rate of poor is %.2f%c.\n",
               bjg, ratebjg, c);
    }
}

int main() {
    char name[30][100];
    long num[30];
    int score[30][6], sumstu[30], rank[30];
    int m, n, a, b, c;  // a for choice,b for times,c for continue;
    for (b = 0; b <= 12; b++) {
        printf("LIST:\n");
        printf("1.Input record\n");
        printf("2.Calculate total and average score of every course\n");
        printf("3.Calculate total and average score of every student\n");
        printf("4.Sort in descending order by total score of every student\n");
        printf("5.Sort in ascending order by total score of every student\n");
        printf("6.Sort in ascending order by number\n");
        printf("7.Sort in dictionary order by name\n");
        printf("8.Search by number\n");
        printf("9.Search by name\n");
        printf("10.Statistic analysis for every course\n");
        printf("11.List record\n");
        printf("0.Exit\n");
        printf("Please enter your choice:");
        scanf("%d", &a);
        switch (a) {
            case 1: {
                printf("Please input the number of the students:");
                scanf("%d", &m);
                printf("Please input the number of the courses:");
                scanf("%d", &n);
                ReadName(name, num, score, m, n);
                break;
            }
            case 2:
                FindCourAve(score, m, n);
                break;
            case 3:
                FindStuAve(score, num, m, n, sumstu);
                break;
            case 4:
                SortDesScore(sumstu, num, name, m, rank);
                break;
            case 5:
                SortAscScore(sumstu, num, name, m);
                break;
            case 6:
                SortAscNum(num, name, score, m, n);
                break;
            case 7:
                SortDicName(name, num, score, n, m);
                break;
            case 8:
                Searbynum(name, num, score, m, n, rank);
                break;
            case 9:
                SearbyName(name, num, score, m, n, rank);
                break;
            case 10:
                Classify(score, m, n);
                break;
            case 11: {
                Output(name, num, score, m, n);
                FindCourAve(score, m, n);
                break;
            }
            case 0:
                return 0;
        }
        printf("\ncontinue(1) or not(2)");
        scanf("%d", &c);
        if (c == 1)
            continue;
        else if (c == 2)
            break;
    }

    return 0;
}
