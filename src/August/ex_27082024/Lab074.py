#local variables has more prefrence to public variables

def home():
    private_toilet ="PT"
    public_toilet="LPT"
    print(public_toilet)
    print(private_toilet)

def stranger():
    print(public_toilet)

print(public_toilet)

home()
stranger()