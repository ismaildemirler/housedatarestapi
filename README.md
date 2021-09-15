<h2><a id="user-content-hi-there-" class="anchor" aria-hidden="true" href="#hi-there-"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>House Rental Information Demo Project</h2>
        <p>
    This project was developed in Django Framework as a Rest API. The language is Python. The Rest API has been created to give some chart results about demo house prices. The first chart is a time series view of average prices for the given postcode and between the given from and to dates, separated by flats, terraced homes, detached homes and semi-detached homes. The second chart is a histogram showing the number of transactions at various price brackets. Note that price brackets will be different in different postcodes and date ranges so you should find a way to automatically generate the price brackets. However, you can keep the number of brackets constant, to say 8. Postgresql database populated to use a management command utilising Django ORM.
    </p>

<p>

<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; First of all postgresql database and addressdata table were created. To create housesdata table executed sql code that shown below: </span> </br>
CREATE TABLE IF NOT EXISTS public.housesdata </br>
( </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  houseid uuid unique,     </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  price integer,     </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  transactiondate date,     </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  postcode character varying(50),   </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  hometype character varying(1),    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  unknown1 character varying(1), //I could not understand what these columns mean. So i called unkowns.     </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  unknown2 character varying(1), //And this unknown columns does not matter in coding task. So i called like that.  </br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  paon character varying(150),   </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  saon character varying(150),     </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  street character varying(150),    </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  locality character varying(150),     </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  town character varying(150),     </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  district character varying(150),    </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  county character varying(150),   </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  unknown3 character varying(1),  </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  unknown4 character varying(1),   </br>
) </br>
	</p>

<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Second, database and table were created, to populate database from csv file i executed the code: </span>

<pre> copy public.housesdata from 'my-csv-file-path/pp-monthly-update-new-version.csv' DELIMITER ',' csv HEADER; </pre>

After required coding process for example for the first graph rest api gives the result shown below:

<pre>GET /api/averagehouseprices/?post_code=N&&beginning_date=2002-11&&end_date=2003-3 </pre>

HTTP 200 OK </br>
Allow: GET, POST, HEAD, OPTIONS </br>
Content-Type: application/json </br>
Vary: Accept </br>

[</br>
&nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 293500.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "200211",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "D"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 56500.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "200211",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "F"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 121500.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "200211",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "S"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 217000.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "200212",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "F"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 170000.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "20031",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "F"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 125000.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "20031",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "T"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 91527.5,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "20032",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "D"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 231150.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "20032",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "S"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"average_price": 65000.0,</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"year_month": "20032",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"home_type": "T"</br>
    &nbsp;&nbsp;&nbsp;&nbsp;}</br>
]</br>


For example for the second graph rest api gives the result shown below:

<pre> GET /api/numberoftransactions/?transaction_date=2003-11 </pre>

HTTP 200 OK</br>
Allow: GET, POST, HEAD, OPTIONS</br>
Content-Type: application/json</br>
Vary: Accept</br>

[</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "Under €130k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 3</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "€130k - €220k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 1</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "€220k - €310k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 1</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "€310k - €400k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 1</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "€400k - €490k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 0</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "€490k - €580k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 0</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "€580k - €670k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 1</br>
    &nbsp;&nbsp;&nbsp;&nbsp;},</br>
    &nbsp;&nbsp;&nbsp;&nbsp;{</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"price_range": "Over €670k",</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_count": 0</br>
    &nbsp;&nbsp;&nbsp;&nbsp;}</br>
]</br>



