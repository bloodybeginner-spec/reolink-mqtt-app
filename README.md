# Reolink MQTT Bridge Add-on for Home Assistant

Dieses Add-on integriert KI-Events (Person, Fahrzeug, Tier, Paket) der Reolink RLC-520A 
und anderer kompatibler Kameras direkt in Home Assistant über MQTT.

Es nutzt die neue Reolink-API (Token-Login + Event-Stream) und erzeugt echte 
Home Assistant Binary Sensoren über MQTT Auto-Discovery.

## Funktionen

- Token-basierter Login in die Kamera
- Abonnieren des KI-Eventstreams
- Erkennen von:
  - Person
  - Fahrzeug
  - Tier
  - Paket
- MQTT-Publishing der Events
- Auto-Discovery für Home Assistant
- Vollständig kompatibel mit Home Assistant OS (Supervisor Add-on)

## Installation

1. Repository zu Home Assistant hinzufügen:

   **Einstellungen → Add-ons → Add-on Store → Repositories → Repository hinzufügen**

   URL:https://github.com/bloodybeginner-spec/reolink-mqtt-addon

2. Add-on installieren
3. Kamera-IP, Benutzername und Passwort eintragen
4. MQTT-Daten eintragen (Mosquitto Add-on)
5. Add-on starten

## Konfiguration

| Option        | Beschreibung                         |
|---------------|--------------------------------------|
| camera_host   | IP der Kamera                        |
| camera_user   | Benutzername (z. B. admin)           |
| camera_pass   | Passwort der Kamera                  |
| mqtt_host     | MQTT-Server (bei HAOS: 127.0.0.1)    |
| mqtt_user     | MQTT-Benutzer                        |
| mqtt_pass     | MQTT-Passwort                        |

## MQTT Topics

- `reolink/person`
- `reolink/vehicle`
- `reolink/pet`
- `reolink/package`

## Home Assistant Entitäten

- `binary_sensor.reolink_person`
- `binary_sensor.reolink_vehicle`
- `binary_sensor.reolink_pet`
- `binary_sensor.reolink_package`

## Kompatibilität

Getestet mit:

- Reolink RLC-520A  
- Firmware v3.2.0.5180_2507241369  
- Home Assistant OS  
- Mosquitto MQTT Add-on  

## Lizenz

MIT License
