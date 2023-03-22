class Student {
  final int regno;
  final String name;
  final String section;
  final String course;
  final String dob;
  final String block;
  final String email;
  final String mobileNumber;
  final String parentsNumber;
  final String coOrdinator;
  final String boardingPoint;
  final String acedemicYear;
  Student({
    required this.section,
    required this.name,
    required this.course,
    required this.dob,
    required this.block,
    required this.email,
    required this.mobileNumber,
    required this.parentsNumber,
    required this.coOrdinator,
    required this.boardingPoint,
    required this.acedemicYear,
    required this.regno,
  });

  factory Student.fromJson(Map<String, dynamic> json) {
    return Student(
      regno: int.parse(json["regno"]),
      name: json["Name"],
      section: json["Section"],
      course: json["course"],
      dob: json["DOB"],
      block: json["Block"],
      email: json["Email"],
      mobileNumber: json["Mobile Number"],
      parentsNumber: json["Parents Number"],
      coOrdinator: json["Co-ordinator"],
      boardingPoint: json["Boarding Point"],
      acedemicYear: json["Acedemic Year"],
    );
  }

  Map<String, dynamic> toJson() => {
        "regno": regno,
        "Name": name,
        "Section": section,
        "course": course,
        "DOB": dob,
        "Block": block,
        "Email": email,
        "Mobile Number": mobileNumber,
        "Parents Number": parentsNumber,
        "Co-ordinator": coOrdinator,
        "Boarding Point": boardingPoint,
        "Acedemic Year": acedemicYear,
      };
}
