create table tg_users
(
    id      bigserial PRIMARY KEY,
    user_id BIGINT NOT NULL UNIQUE,
    active  boolean DEFAULT FALSE,
    key_id  INTEGER NULL DEFAULT NULL
);

alter table tg_users
    owner to postgres;