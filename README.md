# Boilerplate of Python web application(Flask) with GraphQL

English | [Español](./README-es_ES.md)

[![CircleCI branch](https://img.shields.io/circleci/build/github/melonmochi/flask-graphql-boilerplate/master.svg?style=flat-square)](https://circleci.com/gh/melonmochi/flask-graphql-boilerplate) [![Codecov](https://img.shields.io/codecov/c/github/melonmochi/flask-graphql-boilerplate/master.svg?style=flat-square)](https://codecov.io/gh/melonmochi/flask-graphql-boilerplate/branch/master) [![Requirements Status](https://requires.io/github/melonmochi/flask-graphql-boilerplate/requirements.svg?branch=master)](https://requires.io/github/melonmochi/flask-graphql-boilerplate/requirements/?branch=master)

## ⌨️ Development

### ♊ (Recommended) Setup Python virtual enviroment

```bash
python -m venv env
```

Linux:

```bash
source env/bin/activate
```

Windows:

```bash
env\Scripts\activate
```

### 📦 Install dependencies

```python
pip install -r requirements.txt
```

## 🏃 Run

```python
flask run
```

## 🦋 Examples

### 🗄️ RESTful like API

<https://kthhld4776.execute-api.eu-west-1.amazonaws.com/dev/departments>:

```json
[{"id":"d001","name":"Marketing"},{"id":"d002","name":"Finance"},{"id":"d003","name":"Human Resources"},{"id":"d004","name":"Production"},{"id":"d005","name":"Development"},{"id":"d006","name":"Quality Management"},{"id":"d007","name":"Sales"},{"id":"d008","name":"Research"},{"id":"d009","name":"Customer Service"}]
```

### ⛓️ GraphQL like API

<https://kthhld4776.execute-api.eu-west-1.amazonaws.com/dev/graphql>

```yaml
{
  departments(q: "es"){
    deptName
  }
  department(deptNo: "d003"){
    deptNo
    deptName
  }
  employees(
    filters: {
      isManager: true
      or: [
        {empNoRange: { begin: "10030", end: "10050" }}
        {lastNameIlike: "%a%"}
        {firstNameIlike: "%b%"}
        {gender: "F"},
        {birthDateRange: { begin: "1964-02-01", end: "1974-02-01"}}
      ]}
    first: 10
    sort: [LAST_NAME_ASC, FIRST_NAME_ASC]
  ){
    totalCount
    edges{
      node{
        empNo
        birthDate
        firstName
        lastName
        gender
        hireDate
      }
    }
    pageInfo{
      hasPreviousPage,
      hasNextPage,
      startCursor,
      endCursor,
    }
  }
  employee(empNo: "10003"){
    empNo
    firstName
    lastName
  }
}
```

response:

```json
{
  "data": {
    "departments": [
      {
        "deptName": "Human Resources"
      },
      {
        "deptName": "Sales"
      },
      {
        "deptName": "Research"
      }
    ],
    "department": {
      "deptNo": "d003",
      "deptName": "Human Resources"
    },
    "employees": {
      "totalCount": 17,
      "edges": [
        {
          "node": {
            "empNo": "10065",
            "birthDate": "1963-04-14",
            "firstName": "Satosi",
            "lastName": "Awdeh",
            "gender": "M",
            "hireDate": "1988-05-18"
          }
        },
        {
          "node": {
            "empNo": "10077",
            "birthDate": "1964-04-18",
            "firstName": "Mona",
            "lastName": "Azuma",
            "gender": "M",
            "hireDate": "1990-03-02"
          }
        },
        {
          "node": {
            "empNo": "10003",
            "birthDate": "1959-12-03",
            "firstName": "Parto",
            "lastName": "Bamford",
            "gender": "M",
            "hireDate": "1986-08-28"
          }
        },
        {
          "node": {
            "empNo": "10039",
            "birthDate": "1959-10-01",
            "firstName": "Alejandro",
            "lastName": "Brender",
            "gender": "M",
            "hireDate": "1988-01-19"
          }
        },
        {
          "node": {
            "empNo": "10044",
            "birthDate": "1961-09-21",
            "firstName": "Mingsen",
            "lastName": "Casley",
            "gender": "F",
            "hireDate": "1994-05-21"
          }
        },
        {
          "node": {
            "empNo": "10035",
            "birthDate": "1953-02-08",
            "firstName": "Alain",
            "lastName": "Chappelet",
            "gender": "M",
            "hireDate": "1988-09-05"
          }
        },
        {
          "node": {
            "empNo": "10022",
            "birthDate": "1952-07-08",
            "firstName": "Shahaf",
            "lastName": "Famili",
            "gender": "M",
            "hireDate": "1995-08-22"
          }
        },
        {
          "node": {
            "empNo": "10014",
            "birthDate": "1956-02-12",
            "firstName": "Berni",
            "lastName": "Genin",
            "gender": "M",
            "hireDate": "1987-03-11"
          }
        },
        {
          "node": {
            "empNo": "10100",
            "birthDate": "1953-04-21",
            "firstName": "Hironobu",
            "lastName": "Haraldson",
            "gender": "F",
            "hireDate": "1987-09-21"
          }
        },
        {
          "node": {
            "empNo": "10084",
            "birthDate": "1960-05-25",
            "firstName": "Tuval",
            "lastName": "Kalloufi",
            "gender": "M",
            "hireDate": "1995-12-15"
          }
        }
      ],
      "pageInfo": {
        "hasPreviousPage": false,
        "hasNextPage": true,
        "startCursor": "YXJyYXljb25uZWN0aW9uOjA=",
        "endCursor": "YXJyYXljb25uZWN0aW9uOjk="
      }
    },
    "employee": {
      "empNo": "10003",
      "firstName": "Parto",
      "lastName": "Bamford"
    }
  }
}
```

## 🤝 Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

We welcome all contributions.

## 🌍 License

[MIT](https://github.com/melonmochi/flask-graphql-boilerplate/blob/master/LICENSE)
