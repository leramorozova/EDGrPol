import sqlite3
import csv


def makefile():
    conn = sqlite3.connect('GrPolDict.db')
    db = conn.cursor()
    try:
        db.execute("DROP TABLE IF EXISTS articles")
        db.execute("""
                CREATE TABLE articles
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                lemma_rus TEXT NOT NULL,
                deriv_source TEXT NOT NULL,
                pos TEXT NOT NULL,
                lemma_orig TEXT NOT NULL,
                if_hapax TEXT NOT NULL,
                if_middle_lang TEXT NOT NULL,
                vasmer TEXT NOT NULL,
                translated_srcs TEXT NOT NULL,
                rewrit_date TEXT NOT NULL,
                orig_creation TEXT NOT NULL,
                theme TEXT NOT NULL,
                lang TEXT NOT NULL,
                etymology TEXT NOT NULL,
                semantics TEXT NOT NULL,
                slavic_dict TEXT NOT NULL,
                orig_srcs TEXT NOT NULL,
                citation TEXT NOT NULL,
                add_philol TEXT NOT NULL,
                add_histor TEXT NOT NULL,
                historic_sources TEXT NOT NULL,
                slavic_sources TEXT NOT NULL,
                phonetic_variants TEXT NOT NULL,
                morph_variants TEXT NOT NULL,
                linking_references TEXT NOT NULL);
                """)
        print("Tables has been created successfully")
    except Exception as e:
        print("Creation of tables failed in makefile.make_greek:\n")
        print(e)


def data_generator(lang):
    lang = "greek" if lang == "греч." else "polish"
    with open(lang + ".csv", 'r', encoding='UTF-8') as table:
        reader = list(csv.reader(table, delimiter=','))
        for row in reader[1:]:
            yield row


def fill_simple_fields(lang):
    print("filling simple data...")
    conn = sqlite3.connect('GrPolDict.db')
    db = conn.cursor()
    for row in data_generator(lang):
        lemma = row[0].strip("\n")
        deriv_source = row[1].strip("\n")
        lemma_orig = row[2].strip("\n")
        pos = row[3].strip("\n")
        if_hapax = row[7].strip("\n")
        if_middle_lang = row[8].strip("\n")
        vasmer = row[10].strip("\n")
        translated_srcs = row[13].strip("\n")
        rewrit_date = row[15].strip("\n")
        orig_creation = row[16].strip("\n")
        theme = row[18].strip("\n")
        etymology = row[6].strip("\n")
        semantics = row[9].strip("\n")
        slavic_dict = row[12].strip("\n")
        orig_srcs = row[14].strip("\n")
        citation = row[17].strip("\n")
        add_philol = row[19].strip("\n")
        add_histor = row[20].strip("\n")
        historic_sources = row[11].strip("\n")
        slavic_sources = row[12].strip("\n")
        phonetic_variants = row[4].strip("\n")
        morph_variants = row[5].strip("\n")
        linking_references = row[21].strip("\n")
        db.execute(f'''
                INSERT INTO articles
                (deriv_source, lemma_rus, pos, lemma_orig, if_hapax, if_middle_lang,
                vasmer, translated_srcs, rewrit_date, orig_creation, theme, lang,
                etymology, semantics, slavic_dict, orig_srcs, citation, add_philol, add_histor, historic_sources,
                slavic_sources, phonetic_variants, morph_variants, linking_references)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (deriv_source, lemma, pos, lemma_orig, if_hapax, if_middle_lang,
                      vasmer, translated_srcs, rewrit_date, orig_creation, theme, lang,
                      etymology, semantics, slavic_dict, orig_srcs, citation, add_philol, add_histor, historic_sources,
                      slavic_sources, phonetic_variants, morph_variants, linking_references))
        conn.commit()
    print("simple data has been filled successfully!")


def process_greek():
    print("Starting greek processing...")
    lang = "греч."
    fill_simple_fields(lang)
    print("greek has been processed!\n")


def process_polish():
    print("Starting polish processing...")
    lang = "польск."
    fill_simple_fields(lang)
    print("polish has been processed!\n")


def main():
    makefile()
    process_greek()
    process_polish()
    return 0


if __name__ == "__main__":
    main()
