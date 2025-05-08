#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 256

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s filename.itx\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("Error: Cannot open file %s\n", argv[1]);
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), file)) {
        // Remove trailing newline character
        line[strcspn(line, "\n")] = '\0';

        // Ignore empty lines
        if (strlen(line) == 0) {
            continue;
        }

        char output[] = "output";

        // output
        if (strcmp(line, output)) {
            printf("%s\n", line);
        }
    }

    fclose(file);
    return 0;
}
