--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dog_2022; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dog_2022 (
    id integer NOT NULL,
    actors character varying(250),
    directors character varying(250)
);


ALTER TABLE public.dog_2022 OWNER TO postgres;

--
-- Name: dog_2022_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dog_2022_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dog_2022_id_seq OWNER TO postgres;

--
-- Name: dog_2022_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dog_2022_id_seq OWNED BY public.dog_2022.id;


--
-- Name: enforcer2022; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enforcer2022 (
    id integer NOT NULL,
    actors character varying(250),
    directors character varying(250)
);


ALTER TABLE public.enforcer2022 OWNER TO postgres;

--
-- Name: enforcer2022_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.enforcer2022 ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.enforcer2022_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: fall2022; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fall2022 (
    id integer NOT NULL,
    actors character varying(250),
    directors character varying(250)
);


ALTER TABLE public.fall2022 OWNER TO postgres;

--
-- Name: fall2022_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fall2022_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fall2022_id_seq OWNER TO postgres;

--
-- Name: fall2022_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fall2022_id_seq OWNED BY public.fall2022.id;


--
-- Name: shotgun_wedding2022; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shotgun_wedding2022 (
    id integer NOT NULL,
    actors character varying(250),
    directors character varying(250)
);


ALTER TABLE public.shotgun_wedding2022 OWNER TO postgres;

--
-- Name: shotgun_wedding2022_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shotgun_wedding2022_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shotgun_wedding2022_id_seq OWNER TO postgres;

--
-- Name: shotgun_wedding2022_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shotgun_wedding2022_id_seq OWNED BY public.shotgun_wedding2022.id;


--
-- Name: dog_2022 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog_2022 ALTER COLUMN id SET DEFAULT nextval('public.dog_2022_id_seq'::regclass);


--
-- Name: fall2022 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fall2022 ALTER COLUMN id SET DEFAULT nextval('public.fall2022_id_seq'::regclass);


--
-- Name: shotgun_wedding2022 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shotgun_wedding2022 ALTER COLUMN id SET DEFAULT nextval('public.shotgun_wedding2022_id_seq'::regclass);


--
-- Data for Name: dog_2022; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dog_2022 (id, actors, directors) FROM stdin;
1	Channing Tatum	Channing Tatum
2	Jane Adams	Reid Carolin
3	Kevin Nash	
4	Qorianka Kilcher	
5	Etyhan Suplee	
6	Emmy Raven-Lampman	
7	Nicole LaLiberte	
\.


--
-- Data for Name: enforcer2022; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enforcer2022 (id, actors, directors) FROM stdin;
2	Kate Bosworth	\N
3	Mojean Aria	\N
1	Antonio Banderas	Richard Hughes
\.


--
-- Data for Name: fall2022; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fall2022 (id, actors, directors) FROM stdin;
1	Grace Caroline Currey	Scott Mann
2	Virginia Gardner	
3	Mason Gooding	
4	Jeffrey Dean Morgan	
5	Darrell Dennis	
\.


--
-- Data for Name: shotgun_wedding2022; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shotgun_wedding2022 (id, actors, directors) FROM stdin;
\.


--
-- Name: dog_2022_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dog_2022_id_seq', 7, true);


--
-- Name: enforcer2022_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.enforcer2022_id_seq', 3, true);


--
-- Name: fall2022_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fall2022_id_seq', 5, true);


--
-- Name: shotgun_wedding2022_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shotgun_wedding2022_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

