student_data={
"id1": {"name":"harsha","grade":"7","fav subjects":"math,science,SST"},
"id2" : {"name":"sai","grade":"7","fav subjects":"math,science,SST"},
"id3" : {"name":"harsha","grade":"7","fav subjects":"math,science,SST"}

}

result={}
seen=set()

for student_id,details in student_data.items():
    unique_key=(details["name"],details["grade"],details["fav subjects"])
    if unique_key  not in seen:
        seen.add(unique_key)
        result[student_id]=details

for key,value in result.items():
    print(key,value)

