## Поставить пароль в привелигированный режим
Вне зависимости от того будет ли аутентификация пользователя или нет, можно поставить пароль на права админа.
- `en` - Turn on privileged commands
- `conf t` - Configure from terminal
- `enable` - Modify enable password parameters
```
en 
conf t
enable password <password>
```
Можно еще добавить секрет, у него приоритет выше.
```
enable secret <password>
```

## Зашифровать пароль и секрет
- `service` - Modify use of network based services
- `service password-encryption` - Encrypt system passwords
```
en 
conf t
service password-encryption 
```

## Добавить аутентификацию в терминал
Для удаленного доступа к коммутатору устанавливается пароль, нужно будет потом еще раз ввести пароль, чтобы получить права админа.
- `username` - Establish user name authentication
```
en
conf t
username <username> privelege <0-15> password <password>
```

## Авторизация на подключение к консоли
- `line` - Configure a terminal line
- `line console 0` - Configure a Primary 
terminal line
- `login` - Enable password checking
- `login local` - Local password checking
- `end` - To end all configuration modes
```
en
conf t
line console 0
login local
end
```

## Настройка IP адрес коммутатора
IP адрес коммутатора всегда настраивается на логических интерфейсах (vlan), а не на физических (fast-ethernet).
- `interface` - Select an interface to 
configure
- `ip` - Interface internet Protocol config commands
- `no shutdown` - Turn on switch
```
en
conf t
interface Vlan1
ip address 192.168.0.1 255.255.255.0
no shutdown
```

## Настройка виртуальной терминальной линии
- `line vty 0 4` - Configure a virtual 
terminal line
- `transport` - Define transport protocols for line
- `transport input` - Define which protocols to use when connecting to the terminal server
- `transport output` - Define which protocols to use for outgoing connections
- `transport input telnet` - Define TCP/IP Telnet protocol to use when connecting to the terminal server
```
en
conf t
line vty 0 4
transport input telnet
login local
```

## Подключиться к коммутатору через Telnet
CMD:
```cmd
telnet <ip-address>
```

## Создать локальную сеть
- `vlan` - выбрать локальную сеть
- `name` - задать имя локальной сети
```
en
conf t
vlan <0-4094>
name <vlan-name>
```

## Определить подключения для конкретной локальной сети
- `switchport mode access` - связь PC-Swtich
- `switchport access vlan` - определить к какой локальной сети он будет принадлежать
```
en
conf t
interface fa<0/1-0/12>
switchport mode access
switchport access vlan <0-4094>
```

## Настройка IP адресов для конкретной локальной сети
Если ПК находится в локальной сети под номером "3", тогда его IP адрес должен быть таким: 192.168.`3`.1

Для сети под номером "2" - 192.168.`2`.1

## Подключить два коммутатора между собой
Так как коммутаторы находятся в одной модели OSI, нужно использовать кабель Cross-Over. Настройки конфигурации нужно сделать в обоих коммутаторах.
- `switchport mode trunk` - связь Switch-Switch
- `switchport trun allowed vlan` - к каким локальным сетям есть доступ
```
en
conf t
interface gi<0/1-0/2>
switchport mode trunk
switchport trunk allowed vlan <0-4094>
wr mem
```

## Как узнать корневой коммутатор
Должен быть текст `This bridge is the root`
- `sh spanning-tree` - посмотреть STP настройки
```
en
sh spanning-tree
```

## Как включить режим RSTP
Эту команду надо использовать во всех коммуматорах, где должен быть протокол RSTP
- `spanning-tree mode rapid-pvst` - включить режим в RSTP в этом коммутаторе
```
en
conf t
spanning-tree mode rapid-pvst 
```

## Агрегирование каналов
Создаем один логический интерфейс, который объединяет несколько физических интерфейсов.
- `interface range fa<0/1>-<12>` - настройка сразу нескольких интерфейсов
- `channel-group <1-6> mode <mode>`
EtherChannel/Port bundling configuration

Channel Group Modes:
- `active` - Enable LACP unconditionally
- `auto` - Enable PAgP only if a PAgP device is detected
- `desirable` - Enable PAgP uncoditionally
- `on` - Enable EtherChannel only
- `passive` - Enable LACP only if a LACP device is detected
```
en
conf t
interface range fa<0/1>-<12>
channel-group <1-6> mode <mode>
```

## Агрегирование каналов через L3 коммутатор
На коммутаторе L3 уровня вы ставите режим `active`, а на коммутаторах L2 уровня - `passive`.
- `channel-protocol lacp` - Select the channel protocol LACP or PAgP
```
en
conf t
int range fa<0/1>-<12>
channel-protocol <lacp|pagp>
channel-group <1-6> mode <mode>
```

## Посмотреть настройки EtherChannel
```
en
show etherchannel summary
```

## Настройка trunk порта
В случае существовании нескольких `vlan`-ов, `trunk` порт настраивается на ЛОГИЧЕСКОМ интерфейсе.
```
en
conf t
int port-channel <1-12>
switchport mode trunk
```

