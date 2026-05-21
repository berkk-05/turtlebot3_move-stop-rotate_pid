Harika, paket adını `my_pkg` olarak güncelleyip README dosyasını tam istediğin gibi iki net göreve bölelim. Böylece repoya giren hoca veya başka biri, hangi kodun ne işe yaradığını ve nasıl çalıştırılacağını çok net görecek.

Aşağıdaki `README.md` dosyasının içeriğini kopyalayıp kendi dosyana yapıştırabilirsin:

```markdown
# TurtleBot3: Navigation and PID Control 🐢

Bu depo, `my_pkg` ROS paketi altında geliştirilmiş iki farklı otonom mobil robot görevini içermektedir. Görevler, ROS 1 Noetic ortamında TurtleBot3 kullanılarak hazırlanmıştır.

---

## 📍 Görev 1: Engelden Kaçma (Move-Stop-Rotate)
**Dosya:** `scripts/engel_kacma.py`

Bu görevde robot, Lidar sensöründen gelen verileri kullanarak önüne çıkan engellerden kaçınır. Hiçbir hedef gözetmeksizin, sadece hayatta kalma ve çarpışma önleme mantığıyla çalışan reaktif bir durum makinesidir.

* **Move:** Robotun önünde engel yoksa (hedef mesafe temizse), düz bir şekilde ilerler.
* **Stop:** Robot engeli algıladığı an, omuz genişliğini (footprint) koruyacak mesafede motorları durdurur.
* **Rotate:** Engel sensör açısından çıkana kadar kendi ekseni etrafında döner ve önü açıldığında tekrar ilerlemeye başlar.

**Çalıştırmak İçin:**
```bash
rosrun my_pkg engel_kacma.py

```

---

## 🎯 Görev 2: PID ile Mesafe Kontrolü (Distance Control)

**Dosya:** `scripts/pid_kontrol.py`

Bu görevde robot, karşısındaki duvara veya engele belirli bir mesafede (örn: 0.5 metre) pürüzsüz bir şekilde durmak üzere tasarlanmış bir PID (Proportional-Integral-Derivative) kontrolcüsü kullanır.

* **Yumuşak Duruş:** Bang-bang (aç-kapa) kontrolünün aksine, hedefe yaklaştıkça hata payı azaldığı için robotun hızı oransal olarak düşer.
* **Tolerans (Deadband) ve Kilitleme:** Motorlardaki mikro titreşimleri (oscillation) önlemek için ±2 cm'lik bir tolerans aralığı eklenmiştir. Robot hedef aralığa girdiğinde sistemi kilitler ve görevi başarıyla sonlandırır.

**Çalıştırmak İçin:**

```bash
rosrun my_pkg pid_kontrol.py

```

---

## 🛠️ Kurulum ve Ortam Gereksinimleri

* Ubuntu 20.04 & ROS 1 Noetic
* TurtleBot3 simülasyon paketleri (`turtlebot3_gazebo`)

Simülasyon ortamını başlatmak için:

```bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_world.launch

```

## 👨‍💻 Geliştirici

**Ahmet Berk Çetiner** Konya Technical University | RACLAB

```

### Kodları GitHub'a Gönderme Adımları

Hazırladığın bu yeni `README.md` dosyasını ve kodlarını tek bir depoda toplamak için terminalde şu komutları sırasıyla girmen yeterli (link kısmını kendi GitHub kullanıcı adına göre düzenlemeyi unutma):

```bash
# 1. Proje klasörüne git (Eğer workspace içindeysen o klasöre geç)
cd ~/catkin_ws/src/my_pkg

# 2. Git'i başlat
git init

# 3. Dosyaları ekle
git add scripts/engel_kacma.py
git add scripts/pid_kontrol.py
git add README.md

# 4. Commit mesajını yaz
git commit -m "Görev 1 (Move-Stop-Rotate) ve Görev 2 (PID Mesafe) eklendi"

# 5. Ana dalı ayarla
git branch -M main

# 6. GitHub reponu bağla
git remote add origin https://github.com/berkk-05/turtlebot3_basics.git

# 7. Kodları gönder
git push -u origin main

```
