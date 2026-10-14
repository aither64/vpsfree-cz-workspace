import{r as a,j as g}from"./vendor-react-MGxsW2Ms.js";import{c as p,o as x}from"./main-LDE_lf6r.js";const d=`<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src data: blob:; media-src data: blob:; style-src 'unsafe-inline'; font-src data:; form-action 'none'; base-uri 'none'; frame-src 'none'; object-src 'none'" />`;function w(o){const t=o.trim().toLowerCase();return t.startsWith("<!doctype")||t.startsWith("<html")||t.includes("<html")||t.includes("<body")}function y(o){return`<!doctype html><html><head><meta charset="utf-8" />${d}<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root { color-scheme: light; }
  html, body { margin: 0; padding: 0; }
  body {
    padding: 16px;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 14px;
    line-height: 1.45;
    background: #ffffff;
    color: #111827;
    word-break: break-word;
  }
  a { color: #2563eb; }
  pre, code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }
  img { max-width: 100%; height: auto; }
  table { max-width: 100%; }
</style>
</head><body>${o}</body></html>`}function $(o,t){const e=t==="dark"?{text:"#dce7f5",strong:"#ffffff",muted:"#b0c0d6",link:"#ec8c35",linkHover:"#f2a35a",border:"#2a4463",shellBg:"#16273f",tableHeadBg:"#1f3959",quoteBg:"#152741",quoteBorder:"#406a95",codeBg:"#142339",codeText:"#f8fafc",inlineCodeBg:"#1f3959"}:{text:"#16273f",strong:"#16273f",muted:"#64748b",link:"#b75c13",linkHover:"#92400e",border:"#c8d3e3",shellBg:"#ffffff",tableHeadBg:"#e8eef7",quoteBg:"#eef4ff",quoteBorder:"#93c5fd",codeBg:"#f1f5fb",codeText:"#16273f",inlineCodeBg:"#f3f6fb"};return`<!doctype html><html><head><meta charset="utf-8" />${d}<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root { color-scheme: ${t==="dark"?"dark":"light"}; }
  * { box-sizing: border-box; }
  html, body {
    margin: 0;
    padding: 0;
    background: transparent;
  }
  body {
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 14px;
    line-height: 1.6;
    color: ${e.text};
    word-break: break-word;
    overflow-wrap: anywhere;
    background: transparent;
  }
  .helpbox-shell {
    padding: 16px 18px;
    background: ${e.shellBg};
    border: 1px solid ${e.border};
    border-radius: 12px;
  }
  .helpbox-shell > :first-child { margin-top: 0 !important; }
  .helpbox-shell > :last-child { margin-bottom: 0 !important; }
  h1, h2, h3, h4, h5, h6 {
    margin: 1.15em 0 0.6em;
    color: ${e.strong};
    font-weight: 600;
    line-height: 1.25;
  }
  h1 { font-size: 1.25rem; }
  h2 { font-size: 1.125rem; }
  h3 { font-size: 1rem; }
  p, ul, ol, dl, pre, blockquote, table, hr {
    margin: 0 0 0.95em;
  }
  ul, ol {
    padding-left: 1.35rem;
  }
  li + li {
    margin-top: 0.35em;
  }
  a {
    color: ${e.link};
    font-weight: 500;
    text-decoration: none;
    border-bottom: 1px solid ${e.link};
  }
  a:hover {
    color: ${e.linkHover};
    border-bottom-color: ${e.linkHover};
  }
  strong, b {
    color: ${e.strong};
    font-weight: 600;
  }
  small {
    color: ${e.muted};
  }
  hr {
    border: 0;
    border-top: 1px solid ${e.border};
  }
  code {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 0.92em;
    color: ${e.codeText};
    background: ${e.inlineCodeBg};
    border: 1px solid ${e.border};
    border-radius: 6px;
    padding: 0.1rem 0.35rem;
  }
  pre {
    overflow: auto;
    padding: 12px 14px;
    background: ${e.codeBg};
    border: 1px solid ${e.border};
    border-radius: 10px;
  }
  pre code {
    padding: 0;
    border: 0;
    background: transparent;
    color: inherit;
  }
  blockquote {
    margin-left: 0;
    padding: 12px 14px;
    background: ${e.quoteBg};
    border-left: 3px solid ${e.quoteBorder};
    border-radius: 10px;
    color: ${e.muted};
  }
  img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    display: block;
    overflow-x: auto;
  }
  th, td {
    padding: 0.55rem 0.7rem;
    border: 1px solid ${e.border};
    text-align: left;
    vertical-align: top;
  }
  th {
    background: ${e.tableHeadBg};
    color: ${e.strong};
    font-weight: 600;
  }
</style>
</head><body><div class="helpbox-shell">${o}</div></body></html>`}function m(o,t){return new RegExp(`<${t}\\b[^>]*>([\\s\\S]*?)<\\/${t}\\s*>`,"i").exec(o)?.[1]??null}function k(o){const t=m(o,"head")??"",e=m(o,"body")??o;return`<!doctype html><html><head><meta charset="utf-8" />${d}${t}</head><body>${e}</body></html>`}function v(o,t){const e=String(o??""),r=w(e);return r?{srcDoc:k(e),fullDocument:r}:{srcDoc:t.variant==="helpBox"?$(e,t.theme):y(e),fullDocument:!1}}function S(o){const t=o.variant??"default",e=o.theme??"light",{srcDoc:r,fullDocument:h}=a.useMemo(()=>v(o.html,{variant:t,theme:e}),[o.html,e,t]),c=a.useRef(null);return a.useEffect(()=>{if(!o.autoHeight)return;const n=c.current;if(!n)return;const i=()=>{try{const l=n.contentDocument;if(!l)return;const s=Math.max(l.body?.scrollHeight??0,l.documentElement?.scrollHeight??0,96),b=o.maxAutoHeight?Math.max(96,Math.min(s+2,o.maxAutoHeight)):s+2;n.style.height=`${b}px`}catch{}};i(),n.addEventListener("load",i);const u=window.setTimeout(i,0),f=window.setTimeout(i,200);return()=>{n.removeEventListener("load",i),window.clearTimeout(u),window.clearTimeout(f)}},[o.autoHeight,o.maxAutoHeight,r]),g.jsx("iframe",{ref:c,"data-testid":o.testId,title:o.title??x("common.html_preview"),sandbox:"allow-same-origin",referrerPolicy:"no-referrer",allow:"",srcDoc:r,className:p(o.autoHeight?"min-h-24 w-full rounded-md":"h-96 w-full rounded-md",t==="helpBox"&&!h?"border-0 bg-transparent":"border border-border bg-surface",o.className)})}export{S};
