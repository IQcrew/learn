#include <stdio.h>
#include <stdlib.h>

struct student {
    char * name;
    char * surname;
    char gender;
    char * birthDate;
    int birthYear;
    char * kraj;
    double exams[6];
};

char path[] = "C:\\Users\\tobol\\Downloads\\studenti.csv";

struct student * readFile(int *length){
    FILE    *textfile;
    char    *text;
    textfile = fopen(path, "r");
    char numeric[] = {'0','1','2','3','4','5','6','7','8','9','.'};


    //internet start
    long    numbytes;
    fseek(textfile, 0L, SEEK_END);
    numbytes = ftell(textfile);
    fseek(textfile, 0L, SEEK_SET);  
    text = (char*)calloc(numbytes, sizeof(char));   
    fread(text, sizeof(char), numbytes, textfile);
    fclose(textfile);
    //internet end

    int size = 0;
    char * text2 = text;
    while ( *text2++ ) ++size;   
    int index = 0;
    char tempCharArray[size];
    for (size_t h = 0; h < size; h++)
    {
       tempCharArray[h] = '\0';
    }
    int numOfStudents = 1;
    for (int i = 0; i < size; i++)
    {
        if(text[i] == '\n'){numOfStudents++;}
    }
    struct student allStudents[numOfStudents];
    int currentStudentIndex = 0;
    int phase = 1;

    while (index < size)
    {
        struct student newStudent;
        phase = 1;
        while(text[index] != '\n')
        {
            if (phase <= 9){
            int tempI = 0;
            while (text[index] != ';')
            {
                tempCharArray[tempI] = text[index]; index++; tempI++;
            }

            switch (phase)
            {
            case 1:
                newStudent.name = (char*)calloc(tempI, sizeof(char));
                newStudent.surname = (char*)calloc(tempI, sizeof(char));
                int lastSpace = 0;
                for (size_t x = 0; x<tempI; x++)
                {
                    newStudent.name[x] = tempCharArray[x];
                    if(tempCharArray[x] == ' '){lastSpace = x;}
                }
                
                for (size_t i = lastSpace+1; i < tempI; i++)
                {
                    newStudent.surname[i-lastSpace-1] = tempCharArray[i];
                }
                newStudent.name[tempI] = '\000';
                newStudent.surname[tempI-lastSpace-1] = '\000';
                break;
            case 2:
                newStudent.gender = tempCharArray[0];
                break;
            case 3:
                newStudent.birthDate = (char*)calloc(tempI, sizeof(char));
                char tempYear[5];
                tempYear[4] = '\000';
                for (size_t u = 0; u < 4; u++)
                {
                    tempYear[u] = tempCharArray[u];
                }
                newStudent.birthYear = atoi(tempYear);
                for (size_t x = 0; x<tempI; x++)
                {
                    newStudent.birthDate[x] = tempCharArray[x];
                }
                newStudent.birthDate[tempI] = '\000';
                break;
            case 4:
                newStudent.kraj = (char*)calloc(tempI, sizeof(char));
                for (size_t x = 0; x<tempI; x++)
                {
                    newStudent.kraj[x] = tempCharArray[x];
                }
                newStudent.kraj[tempI] = '\000';
                break;
            case 5:
                newStudent.exams[0] = atof(tempCharArray);
                break;
            case 6:
                newStudent.exams[1] = atof(tempCharArray);
                break;
            case 7:
                newStudent.exams[2] = atof(tempCharArray);
                break;
            case 8:
                newStudent.exams[3] = atof(tempCharArray);
                break;
            case 9:
                newStudent.exams[4] = atof(tempCharArray);
                break;

            }
            }
            else if (phase == 10){
            int tempI = 0;
            while (text[index] != ';' && text[index] != '\n')
            {
                tempCharArray[tempI] = text[index]; index++; tempI++;
                int tmp = 0;
                for (int g = 0; g < 11; g++)
                {
                    if(numeric[g] == text[index]){
                        tmp = 1; break;
                    }
                }
                if(text[index] == ';' || text[index] == '\n'){tmp = 1;}
                if(tmp == 0){
                newStudent.exams[5] = atof(tempCharArray);
                index+=100;
                break;
                }
                
            }
            newStudent.exams[5] = atof(tempCharArray);
            }
            
            ++phase;
            if(text[index]!='\n')++index;
            for (size_t h = 0; h < size; h++)
            {
                tempCharArray[h] = '\0';
            }
            
        }
        allStudents[currentStudentIndex] = newStudent;
        currentStudentIndex++;  
        ++index;
    }

    struct student * pointerCopy = (struct student *)calloc(1, sizeof(allStudents));

    for (size_t i = 0; i < numOfStudents; i++)
    {
        pointerCopy[i] = allStudents[i];
    }
    *length = numOfStudents;
    return pointerCopy;
}

void sum(){
    int length = 0;
    struct  student * allStudents = readFile(&length);
    for (int i = 0; i < length; i++)
    {
        printf("%s, nar. %d, ",allStudents[i].name, allStudents[i].birthYear);
        if(allStudents[i].gender == 'm'){ printf("muz");} else{printf("zena");}
        printf(", Kraj: %s\n Vysledky testov: ", allStudents[i].kraj);
        for (size_t r = 0; r < 6; r++)
        {
            printf("%.2f;", allStudents[i].exams[r]);
        }
        printf("\n");
    }
    
}
void who() {}
void best(){
    float best = 0.0f;
    char * name;
    int bestIndex = 0;
    int length = 0;
    struct  student * allStudents = readFile(&length);
    for (int i = 0; i < length; i++){
        for (size_t x = 0; x < 6; x++)
        {
            if(allStudents[i].exams[x] > best){
                best = allStudents[i].exams[x];
                bestIndex = x; name = allStudents[i].name;
            }
        }
    }
    printf("Najlepsi test %.2f\nStudent: %s\nCislo testu %d", best, name, bestIndex+1);

}
void gender(){
    char gender;
    char option[50];
    printf("\nChoose gender (m/f): ");
    scanf("%s", option);
    if(option[0] == 'm'|| option[0] == 'f'){gender = option[0];}
    else{printf("Nespravny vstup\n");return;}
    float best = 0.0f;
    char * name;
    int bestIndex = 0;
    int length = 0;
    struct  student * allStudents = readFile(&length);
    for (int i = 0; i < length; i++){
        for (size_t x = 0; x < 6; x++)
        {
            if( allStudents[i].gender == gender && allStudents[i].exams[x] > best){
                best = allStudents[i].exams[x];
                bestIndex = x; name = allStudents[i].name;
            }
        }
    }
    printf("Najlepsi test %.2f\nStudent: %s\nCislo testu %d", best, name, bestIndex+1);

}
void region() {}
void year() {
    char validChars[] = {'0','1','2','3','4','5','6','7','8','9'};
    int year;
    int studentYear;
    char option[50];
    printf("\nType year: ");
    scanf("%s", option);
    for (size_t i = 0; i < 50; i++)
    {
        if(option[i] == '\000'){break;}
        int tf = 0;
        for (size_t e = 0; e < 10; e++)
        {
            if(validChars[e] == option[i]){tf = 1;break;}
        }
        
        if(tf == 0){
            printf("Nespravny rok!!! (int expected)\n");
            return;
        }
    }
    year = atoi(option);
    float best = 0.0f;
    char * name;
    int bestIndex = 0;
    int length = 0;
    struct  student * allStudents = readFile(&length);
    for (int i = 0; i < length; i++){
        for (size_t x = 0; x < 6; x++)
        {
            if( allStudents[i].birthYear > year && allStudents[i].exams[x] > best){
                best = allStudents[i].exams[x]; studentYear = allStudents[i].birthYear;
                bestIndex = x; name = allStudents[i].name;
            }
        }
    }
    printf("%s\nNar. %d\nNajlepsi test %.2f\nCislo testu %d",name, studentYear, best,  bestIndex+1);
}
void average() {
    int length = 0;
    struct  student * allStudents = readFile(&length);
    double allAvearge[length];
    for (int i = 0; i < length; i++)
    {
        double temp = 0;
        for (size_t x = 0; x < 6; x++)
        {
            temp += allStudents[i].exams[x];
        }
        allAvearge[i] = temp/6;
    }
    int topI = 0;
    for (size_t i = 0; i < length; i++)
    {
        if (allAvearge[i] > allAvearge[topI]){topI = i;}
        printf("%s - %.2f\n", allStudents[i].name, allAvearge[i]);
    }
    printf("\nNajlepsie:\n%s - %.2f", allStudents[topI].name, allAvearge[topI]);
    
}
void over() {
    char validChars[] = {'0','1','2','3','4','5','6','7','8','9','.'};
    char option[50];
    printf("\nType value: ");
    scanf("%s", option);
    for (size_t i = 0; i < 50; i++)
    {
        if(option[i] == '\000'){break;}
        int tf = 0;
        for (size_t e = 0; e < 11; e++)
        {
            if(validChars[e] == option[i]){tf = 1;break;}
        }
        
        if(tf == 0){
            printf("Nespravny vstup!!!\n");
            return;
        }
    }
    int length = 0;
    struct  student * allStudents = readFile(&length);
    double val = atof(option);
    int testOverVal[length];
    for (size_t i = 0; i < length; i++)
    {
        testOverVal[i] = 0;
        for (size_t x = 0; x < 6; x++)
        {
            if(allStudents[i].exams[x] > val){testOverVal[i]++;}
        }
        
    }
    for (size_t i = 0; i < length; i++)
    {
        char * tmp = "test";
        if(testOverVal[i] > 0){
            if(testOverVal[i]> 1){tmp = "testy";}
            printf("%s - %d %s",allStudents[i].name,testOverVal[i],tmp);
            for (size_t x = 0; x < 6; x++)
            {
                if(allStudents[i].exams[x] > val){printf(", %d (%.2f)",x+1,allStudents[i].exams[x]);}
            }
            printf("\n");
        }
    }
    
}
void change() {
    int length = 0;
    struct  student * allStudents = readFile(&length);
    char option[50];
    printf("\nZadaj priezvisko: ");
    scanf("%s", option);
    int tmpIndex;
    int tmpB = 0;
    for (size_t i = 0; i < length; i++)
    {
        if(allStudents[i].surname == option){tmpB = 1;}
        int ready = 1;
        for (size_t x = 0; allStudents[i].surname[x] != '\000'; x++)
        {
            if (allStudents[i].surname[x] != option[x]){ready = 0;}
        }
        if(ready){tmpB = 1; tmpIndex =i; break;}
    }
    if(tmpB == 0){printf("Student z priezviskom %s sa nenasiel", option);return;}

    int cisloTestu;
    printf("\nZadaj cislo testu: ");
    scanf("%d", &cisloTestu);
    if(cisloTestu<1 || cisloTestu > 6){printf("cislo moze byt iba 1-6", option);return;}

    double newVal;
    printf("\nZadaj novu hodnotu: ");
    scanf("%lf", &newVal);
    if(newVal<0 || newVal > 100){printf("cislo moze byt iba od 0 do 100", option);return;}
    allStudents[tmpIndex].exams[cisloTestu-1] = newVal;

    char newText[length*170];
    int idx = 0;
    for (size_t x = 0; x < length; x++)
    {

        for (size_t i = 0; allStudents[x].name[i] != '\000'; i++)
        {
            newText[idx] = allStudents[x].name[i]; idx++;
        }
        newText[idx] = ';';idx++;
        newText[idx] = allStudents[x].gender ;idx++;
        newText[idx] = ';';idx++;
        for (size_t i = 0; allStudents[x].birthDate[i] != '\000'; i++)
        {
            newText[idx] = allStudents[x].birthDate[i]; idx++;
        }
        newText[idx] = ';';idx++;
        for (size_t i = 0; allStudents[x].kraj[i] != '\000'; i++)
        {
            newText[idx] = allStudents[x].kraj[i]; idx++;
        }
        for (size_t z = 0; z < 6; z++)
        {
            newText[idx] = ';';idx++;
            char tempArray[6];
            tempArray[5] = '\000';
            if(allStudents[x].exams[z]< 10){newText[idx] = '0'; idx++; tempArray[4] = '\000';}
            sprintf(tempArray, "%.2f", allStudents[x].exams[z]);
            for (size_t i = 0; tempArray[i] != '\000'; i++)
            {
                newText[idx] = tempArray[i]; idx++;
            }
        }
        if(x!=length-1){newText[idx] = '\n'; idx++;}
    }
    
    printf(newText);

    FILE *file1 = fopen("C:\\Users\\tobol\\Downloads\\studenti.csv", "w");
    int results = fputs(newText, file1);
    fclose(file1);


    printf("\n\n\n\n\n\n\n");
    sum();
}
void newstudent() {}
void delstudent() {

    int length = 0;
    struct  student * allStudents = readFile(&length);
    char option[50];
    printf("\nZadaj priezvisko: ");
    scanf("%s", option);
    int tmpIndex;
    int tmpB = 0;
    for (size_t i = 0; i < length; i++)
    {
        if(allStudents[i].surname == option){tmpB = 1;}
        int ready = 1;
        for (size_t x = 0; allStudents[i].surname[x] != '\000'; x++)
        {
            if (allStudents[i].surname[x] != option[x]){ready = 0;}
        }
        if(ready){tmpB = 1; tmpIndex =i; break;}
    }
    if(tmpB == 0){printf("Student z priezviskom %s sa nenasiel", option);return;}

    char newText[length*170];
    int idx = 0;
    for (size_t x = 0; x < length; x++)
    {
        if(x == tmpIndex){continue; }
        for (size_t i = 0; allStudents[x].name[i] != '\000'; i++)
        {
            newText[idx] = allStudents[x].name[i]; idx++;
        }
        newText[idx] = ';';idx++;
        newText[idx] = allStudents[x].gender ;idx++;
        newText[idx] = ';';idx++;
        for (size_t i = 0; allStudents[x].birthDate[i] != '\000'; i++)
        {
            newText[idx] = allStudents[x].birthDate[i]; idx++;
        }
        newText[idx] = ';';idx++;
        for (size_t i = 0; allStudents[x].kraj[i] != '\000'; i++)
        {
            newText[idx] = allStudents[x].kraj[i]; idx++;
        }
        for (size_t z = 0; z < 6; z++)
        {
            newText[idx] = ';';idx++;
            char tempArray[6];
            tempArray[5] = '\000';
            if(allStudents[x].exams[z]< 10){newText[idx] = '0'; idx++; tempArray[4] = '\000';}
            sprintf(tempArray, "%.2f", allStudents[x].exams[z]);
            for (size_t i = 0; tempArray[i] != '\000'; i++)
            {
                newText[idx] = tempArray[i]; idx++;
            }
        }
        if(x!=length-1){newText[idx] = '\n'; idx++;}
    }
    printf(newText);
    FILE *file1 = fopen("C:\\Users\\tobol\\Downloads\\studenti.csv", "w");
    int results = fputs(newText, file1);
    fclose(file1);

    printf("\n\n\n\n\n\n\n");
    sum();

}


int main(){
    while (1==1)
    {
        char option[50];
        printf("\nChoose option: ");
        scanf("%s", option);
        switch(option[0]){
            case 'x':
                return 0;
                break;
            case 's':
                sum();
                break;
            case 'w':
                who();
                break;
            case 'b':
                best();
                break;
            case 'g':
                gender();
                break;
            case 'r':
                region();
                break;
            case 'y':
                year();
                break;
            case 'a':
                average();
                break;
            case 'o':
                over();
                break;
            case 'c':
                change();
                break;
            case 'n':
                newstudent();
                break;
            case 'd':
                delstudent();
                break;

            default:
                printf("Unknown command!!! \n\n");
                break;
            
        }
    }
    

    return 0;
}
