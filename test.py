import camelot

pdf_path = "output.pdf"
tables = camelot.read_pdf(pdf_path, pages="all")

# Print extracted tables
for i, table in enumerate(tables):
    print(f"Table {i+1}:\n", table.df)  # Convert to pandas DataFrame

# import json
# import base64

# with open('data.json', 'r') as json_file:
#     json_data = json_file.read()

# # Load the JSON response (replace with actual response data)
# json_response = json.loads(json_data)

# # # Decode the base64 string
# # xml_data = base64.b64decode(json_response["documento"]).decode("utf-8")

# # # Save it as an XML file
# # with open("output.xml", "w", encoding="utf-8") as f:
# #     f.write(xml_data)

# # print("XML file saved as output.xml")

# # Convert 'documento' field to bytes (handling negative values correctly)
# binary_data = bytes([(b + 256) if b < 0 else b for b in json_response["documento"]])

# # Save as a PDF file
# with open("output.pdf", "wb") as f:
#     f.write(binary_data)

# print("PDF file saved as output.pdf")
