import re


def main():
    with open('../../inputs/04.txt') as f:
        passports = f.read().split('\n\n')

    passports = (
        dict(field.split(':') for field in passport.split())
        for passport in passports)

    required_fields = 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'

    def has_all_required_fields(passport):
        return all(field in passport for field in required_fields)

    passports = list(filter(has_all_required_fields, passports))
    part1 = len(passports)
    assert part1 == 237

    def is_valid(passport):
        if not 1920 <= int(passport['byr']) <= 2002:
            return False
        if not 2010 <= int(passport['iyr']) <= 2020:
            return False
        if not 2020 <= int(passport['eyr']) <= 2030:
            return False
        hgt = passport['hgt']
        if hgt.endswith('cm'):
            if not 150 <= int(hgt[:-2]) <= 193:
                return False
        elif hgt.endswith('in'):
            if not 59 <= int(hgt[:-2]) <= 76:
                return False
        else:
            return False
        if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
            return False
        if not passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        return len(passport['pid']) == 9 and passport['pid'].isdigit()

    part2 = sum(map(is_valid, passports))
    assert part2 == 172


if __name__ == '__main__':
    main()
