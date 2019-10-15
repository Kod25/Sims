package org.thingsboard.rule.engine.node.googleCalendar;

import lombok.Data;
import org.thingsboard.rule.engine.api.NodeConfiguration;
import java.util.Collection;


@Data
public class TbGoogleCalendarApiCallNodeConfiguration implements NodeConfiguration<TbGoogleCalendarApiCallNodeConfiguration>{

    private String calendarUrl;
    private String requestMethod;
    private String serviceAccountKey;
    private String serviceAccountKeyFileName;

    @Override
    public TbGoogleCalendarApiCallNodeConfiguration defaultConfiguration() {
        TbGoogleCalendarApiCallNodeConfiguration configuration = new TbGoogleCalendarApiCallNodeConfiguration();
        configuration.setCalendarUrl("Calendar Url");
        configuration.setRequestMethod("GET");
        return configuration;
    }
}