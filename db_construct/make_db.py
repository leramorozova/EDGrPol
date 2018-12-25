import sqlite3
import csv


def makefile():
    conn = sqlite3.connect('GrPolDict.db')
    db = conn.cursor()
    try:
        db.execute("DROP TABLE IF EXISTS simple_fields")
        db.execute("""
                CREATE TABLE simple_fields
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                lemma_rus TEXT NOT NULL,
                pos TEXT NOT NULL,
                lemma_greek TEXT NOT NULL,
                if_hapax TEXT NOT NULL,
                if_middle_lang TEXT NOT NULL,
                vasmer TEXT NOT NULL,
                translated_srcs TEXT NOT NULL,
                rewrit_date TEXT NOT NULL,
                orig_creation TEXT NOT NULL,
                theme TEXT NOT NULL,
                lang TEXT NOT NULL);
                """)
        db.execute("DROP TABLE IF EXISTS complex_fields")
        db.execute("""
                    CREATE TABLE complex_fields
                    (lemma TEXT NOT NULL,
                    etymology TEXT NOT NULL,
                    semantics TEXT NOT NULL,
                    slavic_dict TEXT NOT NULL,
                    orig_srcs TEXT NOT NULL,
                    citation TEXT NOT NULL,
                    add_philol TEXT NOT NULL,
                    add_histor TEXT NOT NULL,
                    lang TEXT NOT NULL);
                    """)
        db.execute("DROP TABLE IF EXISTS sources")
        db.execute("""
                CREATE TABLE sources
                (lemma TEXT NOT NULL,
                source TEXT NOT NULL,
                type TEXT NOT NULL,
                lang TEXT NOT NULL);
                """)
        db.execute("DROP TABLE IF EXISTS variants")
        db.execute("""
                    CREATE TABLE variants
                    (lemma TEXT NOT NULL,
                    var_type TEXT NOT NULL,
                    variant TEXT NOT NULL,
                    lang TEXT NOT NULL);
                    """)
        print("Tables has been created successfully")
    except Exception as e:
        print("Creation of tables failed in makefile.make_greek:\n")
        print(e)


def data_generator(lang):
    with open(lang + ".csv", 'r', encoding='UTF-8') as table:
        reader = list(csv.reader(table, delimiter=','))
        for row in reader[1:]:
            yield row


def fill_simple_fields(lang):
    print("filling simple data...")
    conn = sqlite3.connect('GrPolDict.db')
    db = conn.cursor()
    for row in data_generator(lang):
        lemma = row[0]
        greek_lemma = row[2]
        pos = row[3]
        if_hapax = row[7]
        if_middle_lang = row[8]
        vasmer = row[10]
        translated_srcs = row[13]
        rewrit_date = row[15]
        orig_creation = row[16]
        theme = row[18]
        db.execute('''
                INSERT INTO simple_fields
                (lemma_rus, pos, lemma_greek, if_hapax, if_middle_lang,
                vasmer, translated_srcs, rewrit_date, orig_creation, theme, lang)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (lemma, pos, greek_lemma, if_hapax, if_middle_lang,
                      vasmer, translated_srcs, rewrit_date, orig_creation, theme, lang))
        conn.commit()
    print("simple data has been filled successfully!")


def fill_complex_fields(lang):
    print("filling complex data...")
    conn = sqlite3.connect('GrPolDict.db')
    db = conn.cursor()
    for row in data_generator(lang):
        lemma = row[0]
        etymology = row[6]
        semantics = row[9]
        slavic_dict = row[12]
        orig_srcs = row[14]
        citation = row[17]
        add_philol = row[19]
        add_histor = row[20]
        db.execute('''
                    INSERT INTO complex_fields
                    (lemma, etymology, semantics, slavic_dict, orig_srcs, citation, add_philol, add_histor, lang)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (lemma, etymology, semantics, slavic_dict, orig_srcs, citation, add_philol, add_histor, lang))
        conn.commit()
    print("complex data has been filled successfully!")


def fill_sources(lang):
    print("filling sources...")
    conn = sqlite3.connect('GrPolDict.db')
    db = conn.cursor()
    for row in data_generator(lang):
        historic = row[11].split('; ')
        for el in historic:
            if el != '':
                db.execute('''
                INSERT INTO sources
                (lemma, source, type, lang)
                VALUES (?, ?, ?, ?)
               ''', (row[0], el, "hist", lang))
                conn.commit()
        slavic = row[12].split('; ')
        for el in slavic:
            if el != '':
                db.execute('''
                 INSERT INTO sources
                (lemma, source, type, lang)
                VALUES (?, ?, ?, ?)
                ''', (row[0], el, "slavic", lang))
                conn.commit()
    print("sources have been filled successfully")


def fill_variants(lang):
    print("filling variants...")
    conn = sqlite3.connect('GrPolDict.db')
    db = conn.cursor()
    for row in data_generator(lang):
        phonetic = row[4].split(', ')
        for el in phonetic:
            if el != '':
                db.execute('''
                INSERT INTO variants
                (lemma, var_type, variant, lang)
                VALUES (?, ?, ?, ?)
                ''', (row[0], "phon", el, lang))
                conn.commit()
        morph = row[5].split('(')
        if morph[0] != '':
            vars = morph[0].split(', ')
            for var in vars:
                db.execute('''
                INSERT INTO variants
                (lemma, var_type, variant, lang)
                VALUES (?, ?, ?, ?)
                ''', (row[0], "morph", var, lang))
                conn.commit()
    print("variants have been filled successfully")


def process_greek():
    print("Starting greek processing...")
    lang = "greek"
    fill_simple_fields(lang)
    fill_complex_fields(lang)
    fill_sources(lang)
    fill_variants(lang)
    print("greek has been processed!")


def process_polish():
    print("Starting polish processing...")
    lang = "polish"
    fill_simple_fields(lang)
    fill_complex_fields(lang)
    fill_sources(lang)
    fill_variants(lang)
    print("polish has been processed!")


def main():
    makefile()
    process_greek()
    process_polish()
    return 0


if __name__ == "__main__":
    main()
