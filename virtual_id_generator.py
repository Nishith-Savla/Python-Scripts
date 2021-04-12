from PIL import Image
import random
import string
import qrcode


class VirtualId:
    def __init__(self, username, dob, blood_group, mobile_no, address, picture_path):
        self.username = username
        self.id = "".join([random.choice(string.digits) for i in range(10)])
        self.dob = dob
        self.blood_group = blood_group
        self.mobile_no = mobile_no
        self.address = address
        self.profile = Image.open(picture_path)
        self.qr_code = None

    def __str__(self):
        return f"Id Card {{ Username: {self.username}, Id: {self.id}, Date of birth: {self.dob}, Blood Group: {self.blood_group}, Mobile No.: {self.mobile_no}}}"

    def make_qrcode(self):
        img = qrcode.make(self.__str__() + self.profile.show())
        img.save(f"qr_{self.id}.png")


obj = VirtualId("Nishith", "01/10/03", "B+", "9948484737",
                "fkfdkljfdf;djk", "C:/Users/Admin/OneDrive/Pictures/ME/ME_edited.jpg")

print(obj.make_qrcode())
