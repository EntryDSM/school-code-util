# school-code-util
School code parsing and insert to DB

## Usage
place school code xlsx file in same directory (if default provided xls file is deprecated) and run this.

```bash
python -m school_code_util -f <filename> -u <db username> -p <db password>
```
about 15 minute required

## Important
- Please remove first row of xlsx(코드 etc)
- After run, please replace 부속중학교 to 한양대학교 사범대학 부속중학교 and its education_office to 서울특별시 성동광진교육지원청

## Maintainer
- Seonghyeon Kim - [NovemberOscar](https://github.com/NovemberOscar)
