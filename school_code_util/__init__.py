import click
import openpyxl
import pymysql.cursors


@click.command()
@click.option('-f', '--filename', required=True)
@click.option('-u', '--db_username', required=True)
@click.option('-p', '--db_password', required=True)
def main(filename, db_username, db_password):
    query = """
    INSERT INTO school (
    code, 
    school_name, 
    school_full_name, 
    education_office
    ) VALUES (
    %s,
    %s,
    %s,
    %s
    );
    """

    db_connection = pymysql.connect(host="entrydsm.hs.kr",
                                    user=db_username,
                                    password=db_password,
                                    db='louis_vuitton',
                                    charset="utf8mb4",
                                    use_unicode=True,
                                    autocommit=True)

    wb = openpyxl.load_workbook(filename)
    ws = wb.get_sheet_by_name('기관코드 조회자료')

    for r in ws.rows:
        code: str = str(r[0].value)
        school_full_name: str = str(r[1].value)
        school_name: str = str(r[2].value)
        education_office: str = ' '.join(school_full_name.split()[:-1])

        print(f"Inserting {school_name}")

        with db_connection.cursor() as cursor:
            cursor.execute(
                query, (code, school_name, school_full_name, education_office)
            )

        # print(code, "/", school_full_name, "/", school_name, "/", education_office)

    wb.close()


