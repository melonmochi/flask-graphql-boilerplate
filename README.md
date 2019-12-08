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
    isManager
    department{
      deptNo
      deptName
    }
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
      "totalCount": 23,
      "edges": [
        {
          "node": {
            "empNo": "110085",
            "birthDate": "1959-10-28",
            "firstName": "Ebru",
            "lastName": "Alpin",
            "gender": "M",
            "hireDate": "1985-01-01"
          }
        },
        {
          "node": {
            "empNo": "111692",
            "birthDate": "1954-10-05",
            "firstName": "Tonny",
            "lastName": "Butterworth",
            "gender": "F",
            "hireDate": "1985-01-01"
          }
        },
        {
          "node": {
            "empNo": "110344",
            "birthDate": "1961-09-07",
            "firstName": "Rosine",
            "lastName": "Cools",
            "gender": "F",
            "hireDate": "1985-11-22"
          }
        },
        {
          "node": {
            "empNo": "110567",
            "birthDate": "1964-04-25",
            "firstName": "Leon",
            "lastName": "DasSarma",
            "gender": "F",
            "hireDate": "1986-10-21"
          }
        },
        {
          "node": {
            "empNo": "110420",
            "birthDate": "1963-07-27",
            "firstName": "Oscar",
            "lastName": "Ghazalie",
            "gender": "M",
            "hireDate": "1992-02-05"
          }
        },
        {
          "node": {
            "empNo": "111784",
            "birthDate": "1956-06-14",
            "firstName": "Marjo",
            "lastName": "Giarratana",
            "gender": "F",
            "hireDate": "1988-02-12"
          }
        },
        {
          "node": {
            "empNo": "110511",
            "birthDate": "1957-07-08",
            "firstName": "DeForest",
            "lastName": "Hagimont",
            "gender": "M",
            "hireDate": "1985-01-01"
          }
        },
        {
          "node": {
            "empNo": "110765",
            "birthDate": "1954-05-22",
            "firstName": "Rutger",
            "lastName": "Hofmeyr",
            "gender": "F",
            "hireDate": "1989-01-07"
          }
        },
        {
          "node": {
            "empNo": "111035",
            "birthDate": "1962-02-24",
            "firstName": "Przemyslawa",
            "lastName": "Kaelbling",
            "gender": "M",
            "hireDate": "1985-01-01"
          }
        },
        {
          "node": {
            "empNo": "111534",
            "birthDate": "1952-06-27",
            "firstName": "Hilary",
            "lastName": "Kambil",
            "gender": "F",
            "hireDate": "1988-01-31"
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
      "lastName": "Bamford",
      "isManager": false,
      "department": {
        "deptNo": "d004",
        "deptName": "Production"
      }
    }
  }
}
```

## 🤝 Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

We welcome all contributions.

## 🌍 License

[MIT](https://github.com/melonmochi/flask-graphql-boilerplate/blob/master/LICENSE)
