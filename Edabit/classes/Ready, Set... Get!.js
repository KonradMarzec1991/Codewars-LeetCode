class Challange {

    levelPoints = {
        'VE': 5,
        'EA': 10,
        'ME': 20,
        'HA': 40,
        'VH': 80,
        'EX': 120,
    };

    constructor(id, level) {
        this.id = id;
        this.level = level;
    };

    get points() {
        return this.levelPoints[this.level];
    };
};

class User {

    constructor(name, xp, log) {
        this.name = name;
        this.xp = xp;
        this.log = log;
    };

    newSolvedChallenge = challange => {
        this.xp += challange.points;
        this.log.push(challange.id);
    };

};


user1 = new User('Madam', 0, []);
user2 = new User('Steve', 0, []);

challenge1 = new Challange(1, 'VE');
challenge2 = new Challange(2, 'EA');
challenge3 = new Challange(3, 'ME');
challenge4 = new Challange(4, 'HA');
challenge5 = new Challange(5, 'VH');
challenge6 = new Challange(6, 'EX');

user1.newSolvedChallenge(challenge1);
user1.newSolvedChallenge(challenge4);
user1.newSolvedChallenge(challenge6);

user2.newSolvedChallenge(challenge5);
user2.newSolvedChallenge(challenge3);
user2.newSolvedChallenge(challenge2);