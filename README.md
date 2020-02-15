# Python Weapon Generator

Python script meant to generate weapons and create a json array with those.

## Getting Started

To run the program, copy the repository and run `main.py`

### Prerequisites

I wrote it with Python 3.7, so I guess you need at least this version of python to run this

Also do a `pip install requirements.txt`, Flask is now required since there is an API

## Execution
### CLI : 
Still in the works, not recommended
### WEB API:
The web api is the big bold feature of this project. you basically run `flask run` and boom, you get a REST api that only uses get requests.

## Customization
If you want to change the first word of the weapon's name, you can do so by editing the `names.json` file.

## Built With

Python and Vs Code

## Sample Output
```json
{
    "name": "Artisanal Rifle",
    "type": "ASSAULT_RIFLE",
    "rarity": 5,
    "is_bolt_action": false,
    "dmg": 5,
    "clip_size": 46,
    "max_ammo": 500
}
```

## Authors

* Benoit Arnoult (me)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details



