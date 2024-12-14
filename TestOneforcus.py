from SonicSurface import SonicSurface

focus_distance = 0.18  # 18cm

array = SonicSurface()
array.connect(-1)  # シリアルポート選択

try:
    # 一度焦点を設定する
    array.focusAtPos(0, focus_distance, 0)
    print(f"Focusing at 18cm ahead (y={focus_distance}m).")
    # ここで特にtime.sleepやwhileループは不要
    # 装置はこのまま継続して焦点を出力する
    # プログラムを終了したいときにEnterキー待ちなどを入れておくと良い
    input("Press Enter to stop and disconnect...")
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    # 終了時にオフ
    array.switchOnOrOff(False)
    array.disconnect()
    print("Array disconnected.")
