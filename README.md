# TurtleBot3: Navigation and PID Control 🐢

Bu depo, `my_pkg` ROS paketi altında geliştirilmiş iki farklı otonom mobil robot görevini içermektedir. Görevler, ROS 1 Noetic ortamında TurtleBot3 kullanılarak hazırlanmıştır.

---

## 📍 Görev 1: Engelden Kaçma (Move-Stop-Rotate)
**Dosya:** `src/engel_kacma.py`

Bu görevde robot, Lidar sensöründen gelen verileri kullanarak önüne çıkan engellerden kaçınır. Hiçbir hedef gözetmeksizin, sadece hayatta kalma ve çarpışma önleme mantığıyla çalışan reaktif bir durum makinesidir.

* **Move:** Robotun önünde engel yoksa, düz bir şekilde ilerler.
* **Stop:** Robot engeli algıladığı an, omuz genişliğini (footprint) koruyacak mesafede motorları anında durdurur.
* **Rotate:** Engel sensör açısından çıkana kadar kendi ekseni etrafında döner ve önü açıldığında tekrar ilerlemeye başlar.

**Çalıştırmak İçin:**
    rosrun my_pkg engel_kacma.py

---

## 🎯 Görev 2: PID ile Mesafe Kontrolü (Distance Control)
**Dosya:** `src/pid_kontrol.py`

Bu görevde robot, karşısındaki duvara veya engele tam olarak hedeflenen mesafede (0.5 metre) pürüzsüz bir şekilde durmak üzere tasarlanmış bir PID kontrolcüsü kullanır.

* **Yumuşak Duruş:** Hedefe yaklaştıkça hata payı azaldığı için robotun hızı oransal olarak düşer (PID mantığı).
* **Tolerans (Deadband) ve Kilitleme:** Motorlardaki mikro titreşimleri (oscillation) önlemek için +-2 cm'lik bir tolerans aralığı eklenmiştir. Robot hedef aralığa girdiğinde sistemi kilitler ve görevi başarıyla sonlandırır.

**Çalıştırmak İçin:**
    '''rosrun my_pkg pid_kontrol.py'''

---

## 🛠️ Kurulum ve Ortam Gereksinimleri

* Ubuntu 20.04 & ROS 1 Noetic
* Python 3.x
* TurtleBot3 simülasyon paketleri (`turtlebot3_gazebo`)

**Simülasyon ortamını başlatmak için:**
    '''export TURTLEBOT3_MODEL=waffle'''
    '''roslaunch turtlebot3_gazebo turtlebot3_stage_2.launch'''

