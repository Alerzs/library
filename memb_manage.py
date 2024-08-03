class MemberManager:

    def __init__(self) -> None:
        try:
            with open('members_data.pkl', 'rb') as inp:
                data = pickle.load(inp)
                inp.close()
                self.member_list = data
        except:
            self.member_list = []

    def save_member(self):
        with open('member_data.pkl', 'wb') as otp:
            pickle.dump(self.member_list , otp)




    def add_member(self , name ,code_meli):
        self.name = name
        self.code_meli = code_meli
        for member in self.member_list :
            if member.get_code_meli() == self.code_meli:
                return
        self.member_list.append(self.member)
        

    def show_all_rent(self):
        c = ""
        for member in self.member_list:
            a = member
            b = Member.get_rent_list()
            c = f"{c} \n   {a}  {str(b)} " 
        return c
        
            


    def search_members(self ,code_meli):
        self.code_meli = code_meli
        for member in self.member_list:
            if self.code_meli == member.get_code_meli():
                return member
        return False