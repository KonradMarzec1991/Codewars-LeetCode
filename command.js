db.persons.aggregate([
    {$match: {gender: "female"}},
    {$group: {_id: {state: "$location.state"}, totalPersons: {$sum: 1}}},
    {$sort: {totalPersons: -1}}
]).pretty();


db.persons.aggregate([
    {$match: {"dob.age": {$gt: 50}}},
    {
        $group: {
            _id: {gender: "$gender"},
            countPersons: {$sum: 1},
            avgPersons: {$avg: "$dob.age"}
        }
    },
    {$sort: {avgPersons: 1}}
]).pretty();


db.persons.aggregate([
    {
        $project: {
            _id: 0,
            gender: 1,
            fullName: {
                $concat: [
                    {$toUpper: "$name.first"},
                    " ",
                    {$toUpper: "$name.last"},
                ]
            }
        }
    }
]).pretty();


db.persons.aggregate([
    {
      $project: {
        _id: 0,
        gender: 1,
        email: 1,
        birthdate:  {$toDate: "$dob.date"},
        age: "$dob.age",
        fullName: {
          $concat: [
            { $toUpper: { $substrCP: ['$name.first', 0, 1] } },
            {
              $substrCP: [
                '$name.first',
                1,
                { $subtract: [{ $strLenCP: '$name.first' }, 1] }
              ]
            },
            ' ',
            { $toUpper: { $substrCP: ['$name.last', 0, 1] } },
            {
              $substrCP: [
                '$name.last',
                1,
                { $subtract: [{ $strLenCP: '$name.last' }, 1] }
              ]
            }
          ]
        }
      }
    },
    {
        $group: {
            _id: {birthYear: {$isoWeekYear: "$birthdate"}},
            numPersons: {$sum: 1}
        }
    },
    {
        $sort: {
            numPersons: -1
        }
    }
  ]).pretty();


db.friends.aggregate([
    {
        $unwind: "$hobbies"
    },
    {
        $group: {
            _id: {age: "$age"},
            allHobbies: {$push: "$hobbies"}
        }
    }
]).pretty();


db.friends.aggregate([
    {
        $unwind: "$hobbies"
    },
    {
        $group: {
            _id: {age: "$age"},
            allHobbies: {$addToSet: "$hobbies"}
        }
    }
]).pretty();


db.friends.aggregate([
    {
        $project: {
            _id: 0,
            examScore: {
                $slice: ["$examScores", 1]
            }
        }
    }
]).pretty();


db.friends.aggregate([
    {
        $project: {
            _id: 0,
            name: 1,
            numScores: {
                $size: "$examScores"
            }
        }
    }
]).pretty();