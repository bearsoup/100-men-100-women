import csv
import datetime

# import csv data
input_file = open('data_okc/user_data_public.csv', 'rb')
output_file = open('okc_relevant_data_genbin_05.csv', 'wb')


def process_user_data(row):
    """
    Returns csv-ready data for a user.
    """
    gender = row['d_gender']
    orientation = row['d_orientation']
    gender_orientation = row['gender_orientation']
    age = row['d_age']
    ethnicity = row['d_ethnicity']
    country = row['d_country']
    education_phase = row['d_education_phase']
    religion_type = row['d_religion_type']
    religion_seriosity = row['d_religion_seriosity']
    man_with_100 = row['q13']
    woman_with_100 = row['q14']

    return (
        gender, orientation, gender_orientation, age, ethnicity, country,
        education_phase, religion_type, religion_seriosity,
        man_with_100, woman_with_100
    )


def write_to_csv(input, output):
    """
    Parses csv and extracts relevant rows.
    """
    w = csv.writer(output)
    w.writerow([
        "gender", "orientation", "gender_orientation", "age", "ethnicity", "country",
        "education_phase", "religion_type", "religion_seriosity",
        "man_with_100", "woman_with_100"
    ])

    num_processed = 0  # keep count of users processed
    start_time = datetime.datetime.now()

    print "Extracting relevant data from %s: %s\n" % (input_file, start_time)

    d_reader = csv.DictReader(input_file)

    for row in d_reader:
        # ignore users who haven't answered both questions or given a gender
        if 'NA' not in row['q13'] and 'NA' not in row['q14'] and 'NA' not in row['gender_orientation']:
            w.writerow(process_user_data(row))

        else:
            pass

        # output progress occassionally to make sure code hasn't stalled
        num_processed += 1
        if num_processed % 1000 == 0:
            print "%s Users Processed: %s" % (num_processed, datetime.datetime.now())

    print "\nDone!\n%s Users Processed in %s" % (num_processed, datetime.datetime.now() - start_time)

write_to_csv(input_file, output_file)
