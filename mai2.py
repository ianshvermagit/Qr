import qrcode

upi_id = input("Enter your upi id = ")

phonepe_url =  f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
pytam_url =  f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url =  f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr = qrcode.make(phonepe_url)
pytam_qr = qrcode.make(pytam_url)
googlepay_qr = qrcode.make(googlepay_url)

phonepe_qr.save('phonepe_qr.png')
pytam_qr.save('pytam_qr.png')
googlepay_qr.save('googlepay_qr.png')

phonepe_qr.show()
pytam_qr.show()
googlepay_qr.show()
