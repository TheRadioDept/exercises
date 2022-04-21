CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

drop table if exists usage; 
drop table if exists device;
drop table if exists employee; 
drop type if exists brand;
drop type if exists dev_type;
drop type if exists use_type; 

create table employee ( 
    id uuid default uuid_generate_v4 () primary key, 
    first_name varchar not null, 
    last_name varchar not null, 
    email varchar, 
    code varchar unique not null
);

create type  brand as enum  ('DELL', 'HP', 'SAMSUNG'); 
create type  dev_type as enum ('Computer', 'Phone', 'Printer');
create table device ( 
    id uuid default uuid_generate_v4 () primary key, 
    description varchar not null, 
    brand brand not null,
    type dev_type not null,  
    code varchar unique 
);

create type use_type as enum ('CHECK_IN', 'CHECK_OUT');
create table usage ( 
    id uuid default uuid_generate_v4 () primary key,  
    date date not null, 
    employee_id uuid  references employee (id) , 
    device_id uuid references device (id), 
    type use_type not null
);
