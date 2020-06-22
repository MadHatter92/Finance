# END NOTE: This works beautifully!!!

import tabula

# Read pdf into list of DataFrame
# df = tabula.read_pdf("test_data.pdf", pages='all')
# print(df)
# # Read remote pdf into list of DataFrame
df2 = tabula.read_pdf("http://www.apmcazadpurdelhi.com/MW_arrivals19-20.pdf")

# # convert PDF into CSV file
tabula.convert_into("test_data.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
# tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all)