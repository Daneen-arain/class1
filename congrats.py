name = input("daneen: ")
achievement = input("certificate: ")

message = f"\n🎉🎊 CONGRATULATIONS, {name.daneen()}! 🎊🎉\n"
message += f"You have successfully achieved: {achievement.certificate()}"
message += "-" * 50  

print(message)
