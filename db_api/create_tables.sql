create table vpn_servers
(
    id      bigserial PRIMARY KEY,
    country VARCHAR(20) NOT NULL,
    api_link VARCHAR(255) NOT NULL UNIQUE,
    UNIQUE (api_link, country)

)
alter table vpn_servers
    owner to postgres;
