package org;

import com.google.api.client.auth.oauth2.Credential;
import com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp;
import com.google.api.client.extensions.jetty.auth.oauth2.LocalServerReceiver;
import com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeFlow;
import com.google.api.client.googleapis.auth.oauth2.GoogleClientSecrets;
import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.auth.oauth2.GoogleCredentials;
import com.google.auth.oauth2.ServiceAccountCredentials;
import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.client.util.DateTime;
import com.google.api.client.util.store.FileDataStoreFactory;
import com.google.api.services.calendar.Calendar;
import com.google.api.services.calendar.CalendarScopes;
import com.google.api.services.calendar.model.Event;
import com.google.api.services.calendar.model.Events;

import java.io.*;
import java.security.GeneralSecurityException;
import java.util.Collections;
import java.util.List;

public class GoogleCalendarApi {
    public static void main(String... args)  throws GeneralSecurityException{
        GoogleCalendarApi gca = new GoogleCalendarApi();
        gca.getEvent();
    }
    public void getEvent() throws GeneralSecurityException{
        try {
            HttpTransport httpTransport = GoogleNetHttpTransport.newTrustedTransport();
            JsonFactory jsonFactory = JacksonFactory.getDefaultInstance();
            // Build service account credential.

            GoogleCredential credential = GoogleCredential
                    .fromStream(getClass().getClassLoader().getResourceAsStream("awesome-pulsar-254807-ec3bbd8a6056.json"))
                    .createScoped(Collections.singleton(CalendarScopes.CALENDAR));

            Calendar calendar = new Calendar.Builder(httpTransport, jsonFactory, credential).setApplicationName("awesome-pulsar-254807").build();

            System.out.printf(String.valueOf(calendar)+'\n');

            DateTime now = new DateTime(System.currentTimeMillis());
            Events events = calendar.events().list("projektlennart@gmail.com")
                    .setMaxResults(10)
                    .setTimeMin(now)
                    .setOrderBy("startTime")
                    .setSingleEvents(true)
                    .execute();
            System.out.println(String.valueOf(events));
            List<Event> items = events.getItems();

            System.out.println("Upcoming events");
            for (Event event : items) {
                DateTime start = event.getStart().getDateTime();
                if (start == null) {
                    start = event.getStart().getDate();
                }
                System.out.printf("%s (%s)\n", event.getDescription(), start);

            }


        }catch(IOException e){System.out.printf(String.valueOf(e));}
    }
}
