COLUMN_MAPPINGS = {
    "RoleCategoryMaster": {
        "RoleCategory": "name",
    },
    "MachineCategoryMaster": {
        "Name": "name",
        "Abbreviation": "abbreviation",
        "Code": "code"
    },
    "GradeMaster": {
        "Grade": "name"
    },
    "RoleMaster": {
        "RoleCategoryId": "roleCategoryId",
        "Role": "name",
        "Abbreviation": "abbreviation",
        "MachineCategoryId": "machineCategoryId",
        "Code": "code"
    },
    "WorkforceDataOverview": {
        "WorkforceId": "workforceId",
        "SeniorityRank": "seniorityRank",
        "CasualRank": "casualRank",
        "RoleId": "roleId",
        "GradeId": "gradeId",
        "SkillsId": "skills"
    },
    "TreadMaster": {
        "TreadCode" : "treadCode",
        "TreadWeight": "treadWeight",
        "Splice" : "splice",
        "GTCode": "gtCode",
    },
    "MachineCategory": {
        "MachineNumber": "machineNumber",
        "MachineCategoryId": "machineCategoryId",
        "TreadId": "treadId",
        "Hoist": "hoist"
    },
    "MachinePreference": {
        "CombinationType": "category",
        "Machine1Id" : "sourceMachineId",
        "Machine2Id": "targetMachineId",
        "PreferenceNumber": "preferenceNumber",
        "Default": "isDefault",
    }
}
