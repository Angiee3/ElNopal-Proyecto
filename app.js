const mysqldump = require('mysqldump')
const nodeCron = require("node-cron");
require('dotenv').config()
const fs = require('fs');
const Path = require('path');
const moment = require('moment');
nodeCron.schedule('*/10 * * * *', ()=>{
        mysqldump({
        connection: {
            host: process.env.DB_HOST,
            user: process.env.DB_USER,
            password: process.env.DB_PASSWORD,
            database: process.env.DB_NAME,
        },
        dump: {schema:{table:{dropIfExist: true}}},
        dumpToFile: `./nopal/static/backup/${process.env.DB_NAME}_${moment().format('YYYY_MM_DD')}_.sql`,
    })
    console.log('base de datos creada ',moment().format('YYYY_MM_DD'));
}, {
    scheduled: true,
    timezone: "America/Bogota"
 });
