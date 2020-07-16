/**
 * Created by J.R(jujin1324@daum.net)
 * Created Date : 2020/07/16
*/

#include <stdio.h>
#include "version.h"

int main() {
    printf("Hello! This Application version is %d.%d.%d", MAJOR, MINOR, PATCH);
    return 0;
}