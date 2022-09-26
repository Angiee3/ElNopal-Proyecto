const mysqldump = require('mysqldump')
const nodeCron = require("node-cron");
require('dotenv').config()
const fs = require('fs');
const Path = require('path');
const moment = require('moment');
nodeCron.schedule('25 */1 * * * *', ()=>{
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

     nodeCron.schedule('*/1 * * * *', ()=>{
        let ruta = './nopal/static/backup'
        let array = []
        if(fs.existsSync(ruta)){
            fs.readdirSync(ruta).forEach((file)=>{
                const curPath = Path.join(ruta, file )
                array.push(curPath)
            }) 
            console.log(array);
            if(array.length >0){
                if(fs.existsSync(array[0])){
                    fs.unlinkSync(array[0])
                    array.shift(array[0],' eliminado');
                    console.log(array , ' recientes' )
                }else{
                    console.log('error no existe');
                }
            }
        }
        console.log('si funciona');
     } ,
     {
     scheduled: true,
     timezone: "America/Bogota"
    })

// let spawn = require('child_process').spawn;
// let wstream = fs.createWriteStream('dumpfilename.sql');
// let comando = spawn('mysqldump', [
//     '-u',
//     `${process.env.DB_USER}`,
//     `-p${process.env.DB_PASSWORD}`,
//     `${process.env.DB_NAME}`,
//     '--tables',
//     'management_category'
// ])
// comando.stdout.pipe(wstream).on('finish', function () {
//         console.log('Completed')
//     })
//     .on('error', function (err) {
//         console.log(err)
//     });